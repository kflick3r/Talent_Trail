'''
Purpose:
    Backend Server for the Talent Trail landing page using Flask. 
    Connects O*NET database(occupation_data) using SQLite and retrieves career information
    Sends that data to the landing page template (career_selection.html)

Usage:
    Run the file to start the Flask Development server for application.
    python career_selection_app.py

Author: Kassidy Flick
'''

from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "Data", "onet.db")



def get_careers():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        SELECT DISTINCT o.onetsoc_code, o.title 
        FROM occupation_data o
        LEFT JOIN skills s ON o.onetsoc_code = s.onetsoc_code
        GROUP BY o.onetsoc_code
        ORDER BY o.title ASC
    """)
    careers = c.fetchall()

    conn.close()
    return careers

def get_skills(onetsoc_code):
    if not onetsoc_code:
        return []
        
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    query = """
        SELECT cmr.element_name, MAX(data_value) as data_value, cmr.description
        FROM skills s
        JOIN content_model_reference cmr ON s.element_id = cmr.element_id
        WHERE s.onetsoc_code = ?
        GROUP BY element_name
        ORDER BY data_value DESC
        LIMIT 10
    """

    c.execute(query, (onetsoc_code,))
    skills = c.fetchall()

    conn.close()
    return skills

print("Database path:", DB_PATH)
print("Careers:", get_careers()[:5])


def get_career_name(onetsoc_code):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT title FROM occupation_data WHERE onetsoc_code = ?", (onetsoc_code,))
    row = cursor.fetchone()
    
    conn.close()
    
    if row:
        return row[0]  # career name/title
    else:
        return "Unknown Career"
#---

@app.route("/")
def career_selection():
    careers = get_careers()
    return render_template("career_selection.html", careers=careers)


@app.route("/survey", methods=["GET","POST"])
def survey():
    onetsoc_code = request.values.get("career")
    print("Received career code:", onetsoc_code)

    if not onetsoc_code:
        return "Error: No career selected", 400

    skills = get_skills(onetsoc_code)

    if not skills:
        return f"No skills found for {onetsoc_code}. Please select another career.", 200

    career_name = get_career_name(onetsoc_code)
    
    return render_template("career_survey.html", skills=skills, career_name=career_name)

#---

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)