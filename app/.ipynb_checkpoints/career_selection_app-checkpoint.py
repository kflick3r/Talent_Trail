'''
Purpose:
    Backend Server for the Talent Trail landing page using Flask. 
    Connects O*NET database(occupation_data) using SQLite and retrieves career information
    Sends that data to the landing page template (landing_page.html)

Usage:
    Run the file to start the Flask Developement server for application.
    python landing_page_app.py

Author: Kassidy Flick
'''

from flask import Flask, render_template

import sqlite3

app = Flask(__name__)

def get_careers():
    conn = sqlite3.connect("Data/onet.db")
    c = conn.cursor()

    c.execute("SELECT onetsoc_code, title FROM occupation_data ORDER BY title ASC")
    careers = c.fetchall()

    conn.close()
    return careers

@app.route("/")
def landing():
    careers = get_careers()
    return render_template("career_selection.html", careers=careers)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    