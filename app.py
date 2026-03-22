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

Author: Kassidy Flick
'''

from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

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

    query = """
        SELECT cmr.element_name, MAX(s.data_value) as data_value, cmr.description
        FROM skills s
        JOIN content_model_reference cmr ON s.element_id = cmr.element_id
        WHERE s.onetsoc_code = ?
        GROUP BY cmr.element_name, cmr.description
        ORDER BY data_value DESC
        LIMIT 10
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
    '''
    Temporary fill-in page.
    Renders results page.
    '''
    return render_template("results.html")

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

