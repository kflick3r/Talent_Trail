'''
Purpose:
    Backend Server for the Talent Trail using Flask. 
    
    - Connects to the O*NET SQLite database(onet.db)  
    - Retrieves career codes and titles to populate dropdown menu on career_selection.html
    - After user selects career, retrieves the top ten unique associated skills
    - Sends career and skill data to career_survey.html

Usage:
    Run the file to start the Flask Development server:
        python app.py
    
    Requirements:
        - Virtual environment activated OR Flask installed locally
            - from project root run (source venv/bin/activate)
        - Database file located at: Data/onet.db
'''

#import pdfkit
from flask import Flask, render_template, request, make_response, session, url_for
import sqlite3
import os
import prefix
import shutil

app = Flask(__name__)

app.config['SESSION_COOKIE_PATH'] = '/'
app.secret_key = "dev-stable-key"

# ------------------------------------------
# PDF loading software based on environment
# ------------------------------------------

wkhtmltopdf_path = shutil.which("wkhtmltopdf")

print("WKHTML PATH:", wkhtmltopdf_path)

def generate_pdf(html):
    import flask

    if wkhtmltopdf_path:
        import pdfkit
        config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

        return pdfkit.from_string(
            html,
            False,
            configuration=config,
            options={
                "enable-local-file-access": ""
            }
        )
    else:
        from weasyprint import HTML
        return HTML(string=html, base_url=flask.request.url_root).write_pdf()

# Only apply prefix in JupyterHub
if "JUPYTERHUB_SERVICE_PREFIX" in os.environ:
    import prefix
    prefix.use_PrefixMiddleware(app)

# Determine the absolute path to database file
# Ensures the app works even if this file is moved
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "Data", "onet.db")


# ----------------------------------------------
# DATABASE FUNCTIONS
# ----------------------------------------------


def get_careers():
    '''
    Retrieves a list of careers that have at least one associated skill.

    Returns:
        List of tuples (onetsoc_code, title)

    Notes: 
        - INNER JOIN ensures only careers with skills are included
        - DISTINCT returns duplicate skills
        - Results are sorted alphabetically by title
    '''

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        SELECT DISTINCT o.onetsoc_code, o.title 
        FROM occupation_data o
        JOIN skills s ON o.onetsoc_code = s.onetsoc_code
        ORDER BY o.title ASC
    """)
    careers = c.fetchall()

    conn.close()
    return careers

def get_skills(onetsoc_code):
    '''
    Retrives the top 10 highest-valued skills for a selected career.

    Parameters:
        onetsoc_code: Unique identifier for career

    Returns:
        List of tuples: (skill_name, data_value, description)

    Notes:
        - Joins skills table with content_model_reference to get readable names and descriptions
        - MAX(data_value) selects the highest score per skill
        - GROUP BY ensures each skill appears only once
        - Results are sorted by importance (descending)
    '''

    if not onetsoc_code:
        return []
        
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    #Changed: Uses scale_id - 'IM' so survey shows 15 most important skills for occupation

    query = """
        SELECT cmr.element_name, s.data_value, cmr.description
        FROM skills s
        JOIN content_model_reference cmr ON s.element_id = cmr.element_id
        WHERE s.onetsoc_code = ?
        AND s.scale_id = 'IM'
        ORDER BY s.data_value DESC
        LIMIT 15
    """

    c.execute(query, (onetsoc_code,))
    skills = c.fetchall()

    conn.close()
    return skills


def get_career_name(onetsoc_code):
    '''
    Retrieves the readable career title from the database.

    Parameter:
        onetsoc_code: Career identifier

    Returns:
        str: Career title OR "Unknown Career" if not found
    '''
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT title FROM occupation_data WHERE onetsoc_code = ?", (onetsoc_code,))
    row = cursor.fetchone()
    
    conn.close()
    
    if row:
        return row[0]  # career name/title
    else:
        return "Unknown Career"

# Debugging output (runs at startup)
print("Database path:", DB_PATH)
print("Sample careers:", get_careers()[:5])


#-----------------------------------------------
# Comparison Functions
#-----------------------------------------------

def get_skill_levels_and_importance(onetsoc_code, skill_names):
    '''
    Pulls the O*NET Level (LV) and Importance (IM) values
    for the selected skills for one occupation.

    Parameters:
        onetsoc_code: selected career code
        skill_names: list of skill names shown on the survey

    Returns:
        list of dictionaries like:
        [
            {
                "skill_name": "Critical Thinking",
                "onet_level": 4.75,
                "onet_importance": 4.25
            }
        ]
    '''

    if not onetsoc_code or not skill_names:
        return []

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Create the right number of ? placeholders for the IN clause
    placeholders = ",".join(["?"] * len(skill_names))

    query = f"""
        SELECT
            cmr.element_name,
            MAX(CASE WHEN s.scale_id = 'LV' THEN s.data_value END) AS onet_level,
            MAX(CASE WHEN s.scale_id = 'IM' THEN s.data_value END) AS onet_importance
        FROM skills s
        JOIN content_model_reference cmr
            ON s.element_id = cmr.element_id
        WHERE s.onetsoc_code = ?
          AND cmr.element_name IN ({placeholders})
          AND s.scale_id IN ('LV', 'IM')
        GROUP BY cmr.element_name
    """

    params = [onetsoc_code] + skill_names
    c.execute(query, params)
    rows = c.fetchall()

    conn.close()

    results = []
    for row in rows:
        results.append({
            "skill_name": row[0],
            "onet_level": float(row[1]) if row[1] is not None else 0,
            "onet_importance": float(row[2]) if row[2] is not None else 0
        })

    return results


def rank_skill_gaps(skill_data, user_ratings):
    '''
    Compares user skill ratings against O*NET data.

    Parameters:
        skill_data: list from get_skill_levels_and_importance()
        user_ratings: dictionary like
            {
                "Critical Thinking": 3,
                "Active Listening": 4
            }

    Returns:
        list of dictionaries sorted by weighted_gap descending
    '''

    results = []

    for skill in skill_data:
        skill_name = skill["skill_name"]
        onet_level = skill["onet_level"]
        onet_importance = skill["onet_importance"]
        user_level = user_ratings.get(skill_name, 0)

        # Raw skill gap
        gap = onet_level - user_level

        # If user is already above the O*NET level,
        # do not treat that as a negative priority
        if gap < 0:
            gap = 0

        # Weight the gap by importance
        importance_weight = onet_importance / 5
        weighted_gap = gap * importance_weight

        results.append({
            "skill_name": skill_name,
            "user_level": user_level,
            "onet_level": round(onet_level, 2),
            "onet_importance": round(onet_importance, 2),
            "gap": round(gap, 2),
            "weighted_gap": round(weighted_gap, 2)
        })

    results.sort(key=lambda x: x["weighted_gap"], reverse=True)
    return results

# move the calculation out of the route function to support PDF creation
def calculate_results(onetsoc_code, user_ratings):
    skill_names = list(user_ratings.keys())

    skill_data = get_skill_levels_and_importance(onetsoc_code, skill_names)
    ranked_results = rank_skill_gaps(skill_data, user_ratings)

    matched_skills = [r["skill_name"] for r in ranked_results if r["gap"] == 0]
    skills_to_improve = [r["skill_name"] for r in ranked_results if r["gap"] > 0]

    if ranked_results:
        compatibility_score = round((len(matched_skills) / len(ranked_results)) * 100)
    else:
        compatibility_score = 0

    return ranked_results, matched_skills, skills_to_improve, compatibility_score


# ----------------------------------------------
# Jupyter Hub proxy-safe URLs
# ----------------------------------------------

@app.context_processor
def implement_script_root():
    return dict(script_root=request.script_root)

# ----------------------------------------------
# ROUTES
# ----------------------------------------------

@app.route("/")
def landing_page():
    '''
    Renders the landing page.
    '''
    return render_template("landing_page.html")

@app.route("/about")
def about_page():
    '''
    Renders the about page.
    '''
    return render_template("about.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")
    
@app.route("/careers")
def career_selection():
    '''
    Renders the career selection page.
    - Loads careers from database
    - Passes them to the template for dropdown display
    '''
    careers = get_careers()
    return render_template("career_selection.html", careers=careers)


@app.route("/careers/survey", methods=["GET","POST"])
def survey():
    '''
    Handles career selection and displays the survey page.

    Workflow:
        1. Get selected career code from request
        2. Validate input
        3. Retrieve associated skills
        4. Retrieve career name
        5. Render survey page with results
    '''
    onetsoc_code = request.values.get("career")
    print("Received career code:", onetsoc_code)

    if not onetsoc_code:
        return "Error: No career selected", 400

    skills = get_skills(onetsoc_code)

    if not skills:
        return f"No skills found for {onetsoc_code}. Please select another career.", 200

    career_name = get_career_name(onetsoc_code)
    
    return render_template("career_survey.html", skills=skills, career_name=career_name, onetsoc_code=onetsoc_code)

@app.route("/careers/survey/results", methods=["POST"])
def results():
    onetsoc_code = request.form.get("career_code")

    if not onetsoc_code:
        return "Error: No career code submitted.", 400

    skills = get_skills(onetsoc_code)
    career_name = get_career_name(onetsoc_code)

    user_ratings = {}
    for idx, (skill_name, value, description) in enumerate(skills):
        rating = request.form.get(f"rating_{idx}")
        if rating is not None:
            user_ratings[skill_name] = int(rating)

    ranked_results, matched_skills, skills_to_improve, compatibility_score = calculate_results(
    onetsoc_code, user_ratings
)
    
    if skills_to_improve:
        top_skills = skills_to_improve[:3]
        if len(top_skills) == 1:
            feedback_message = f"Improving {top_skills[0]} will increase your compatibility with {career_name.lower()} roles."
        elif len(top_skills) == 2:
            feedback_message = f"Improving {top_skills[0]} and {top_skills[1]} will increase your compatibility with {career_name.lower()} roles."
        else:
            feedback_message = f"Improving {top_skills[0]}, {top_skills[1]}, and {top_skills[2]} will increase your compatibility with {career_name.lower()} roles."
    else:
        feedback_message = f"You currently meet or exceed the top measured skill levels for {career_name.lower()}."

    session["results"] = {
    "career_name": career_name,
    "compatibility_score": compatibility_score,
    "matched_skills": matched_skills,
    "skills_to_improve": skills_to_improve,
    "onetsoc_code": onetsoc_code,
    "ranked_results": ranked_results
}
    session.modified = True
    
    print("Stored in session:", session.get("results"))

    return render_template(
        "results.html",
        career_name=career_name,
        compatibility_score=compatibility_score,
        matched_skills=matched_skills,
        skills_to_improve=skills_to_improve,
        feedback_message=feedback_message,
        ranked_results=ranked_results
    )

@app.route("/careers/survey/results/pdf")
def results_pdf():
    data = session.get("results")

    if not data:
        return "No results found.", 400

    html = render_template("results_pdf.html", **data)

    pdf = generate_pdf(html)

    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "attachment; filename=results.pdf"

    return response

# ----------------------------------------------
# APPLICATION LAUNCH / MAIN
# ----------------------------------------------

if __name__ == "__main__":
    ''' 
    Start the Flask developement server
    - host="0.0.0.0" allows access from any IP
    - port=5000 the port the server listens on
    - debug=True enables auto-reload on code changes and shows detailed error messages
    '''
    app.run(host="0.0.0.0", port=5000, debug=True)
