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

    c.execute("SELECT onetsoc_code, title FROM occupation_data ORDER BY title ASC")
    careers = c.fetchall()

    conn.close()
    return careers

def get_skills(onetsoc_code):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    query = """
        SELECT cmr.element_name, s.data_value
        FROM skills s
        JOIN content_model_reference cmr
        ON s.element_id = cmr.element_id
        WHERE s.onetsoc_code = ?
        AND s.scale_id = 'IM'
        ORDER BY s.data_value DESC
        LIMIT 10
    """

    c.execute(query, (onetsoc_code,))
    skills = c.fetchall()

    conn.close()

    return skills

#---

@app.route("/")
def career_selection():
    careers = get_careers()
    return render_template("career_selection.html", careers=careers)


@app.route("/survey", methods=["GET","POST"])
def survey():
    onetsoc_code = request.values.get("career")
    skills = get_skills(onetsoc_code)

    return render_template("career_survey.html", skills=skills)

#---

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)