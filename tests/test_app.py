"""
test_app.py

Purpose: 
    Unit tests for the Talent Trail app.py file:
    Covers:
        - Flask Routes
        - Core Logic
            - Skill Gap
            - Results
        - Edge Cases
    Uses mock data to avoid DB dependencey

Usage: 
    python -m unittest test_app.py
"""

import unittest

# Import Patch for mock data
from unittest.mock import patch, MagicMock

from app import (
    app, 
    rank_skill_gaps, 
    calculate_results, 
    get_skills, 
    get_careers, 
    get_career_name,
)

# -------------------
# Test Flask Routes
# -------------------

class TalentTrailRouteTests(unittest.TestCase):
# Tests Flask Routes and HTML Responses
    
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    # -------------------
    # Landing Page Tests
    # -------------------
    
    def test_landing_page(self):
        # Landing Page should return 200 and contain basic HTML
        
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<html', response.data)

    
    # ---------------------------------------
    # Career Selection Page Tests using patch
    # ---------------------------------------
    
    @patch("app.get_careers")
    def test_career_selection_page(self, mock_careers):
        # Selection page should call get_careers(), render a dropdown, display mock careers
        
        # mock careers with ("onet_code", "career_title")
        mock_careers.return_value = [
            ("1", "Engineer"),
            ("2", "Doctor")
        ]
        
        response = self.client.get('/careers')
        
        self.assertEqual(response.status_code, 200)

        #Check for dropdownn
        self.assertIn(b'<select', response.data)

        #Check if Mock Careers Appear
        self.assertIn(b'Engineer', response.data)
        self.assertIn(b'Doctor', response.data)
        
    # -----------------
    # Survey Page Tests
    # -----------------
    
    def test_survey_page_requires_career_selection(self):
        # Survey page GET without career parameter should return 400
        
        response = self.client.get('/careers/survey')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Error: No career selected', response.data)


    @patch("app.get_skills")
    @patch("app.get_career_name")
    def test_survey_page_with_valid_career(self, mock_name, mock_skills):
        # survey page should display career name, skills, and render form elements (radio buttons, submit)
        
        mock_skills.return_value = [("Python", 5, "desc")]
        mock_name.return_value = "Engineer"

        response = self.client.get('/careers/survey?career=123')
        
        self.assertEqual(response.status_code, 200)

        # Test career name from mock data
        self.assertIn(b'Engineer', response.data)

        # Test skill from mock data
        self.assertIn(b'Python', response.data)

        # Check for UI elements
        self.assertIn(b'<form', response.data)
        self.assertIn(b'type="radio"', response.data)
        self.assertIn(b'type="submit"', response.data)


    # -------------------
    # Results Page Tests
    # -------------------
    
    @patch("app.get_skills")
    @patch("app.get_career_name")
    @patch("app.calculate_results")
    def test_results_route(self, mock_calc, mock_name, mock_skills):
        # Results POST should process user ratings, display career name, mock calculated results
        
        mock_skills.return_value = [("Python", 5, "desc")]
        mock_name.return_value = "Engineer"
        mock_calc.return_value = ([], ["Python"], [], 100)

        response = self.client.post('/careers/survey/results', data={
            "career_code": "123",
            "rating_0": "5"
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Engineer', response.data)

    def test_results_missing_code(self):
        # Results POST without career code should return 400
        
        response = self.client.post('/careers/survey/results', data={})

        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Error: No career code submitted.', response.data)


    # ----------
    # PDF Tests
    # ----------

    def test_results_pdf_success(self):
        with self.client.session_transaction() as session:
            session["results"] = {
                "career_name": "Engineer",
                "compatibility_score": 85,
                "matched_skills": ["Python", "SQL"],
                "skills_to_improve": ["React"],
                "onetsoc_code": "123",
                "ranked_results": []
            }

        response = self.client.get("/careers/survey/results/pdf")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/pdf")
        self.assertTrue(response.data.startswith(B"%PDF"))

    def test_results_pdf_no_session(self):
        response = self.client.get("/careers/survey/results/pdf")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"No results found", response.data)

# -------------------
# Test Core Logic
# -------------------

class TalentTrailLogicTests(unittest.TestCase):
# Tests for skill ranking and results calculation
    
    # ----------------
    # Skill Gap Tests
    # ----------------

    def test_rank_skill_gaps_basic(self):
        # Skill gap should calculate positive gap and weighted gap
        
        skill_data = [
            {"skill_name": "Python", "onet_level": 5, "onet_importance": 5}
        ]

        user = {"Python": 3}

        result = rank_skill_gaps(skill_data, user)

        self.assertEqual(result[0]["gap"], 2)
        self.assertGreater(result[0]["weighted_gap"], 0)

    def test_rank_skill_gaps_no_negative(self):
        # Gap should not be negative
        
        skill_data = [
            {"skill_name": "Python", "onet_level": 5, "onet_importance": 5}
        ]

        user = {"Python": 3}

        results = rank_skill_gaps(skill_data,user)

        self.assertEqual(results[0]["gap"], 2)
        self.assertGreater(results[0]["weighted_gap"], 0)

    def test_rank_skill_gaps_missing_user_skill(self):
        # Default to zero for missing user skill
        
        skill_data = [
            {"skill_name": "Python", "onet_level": 5, "onet_importance": 5}
        ]

        results = rank_skill_gaps(skill_data, {})
        self.assertEqual(results[0]["user_level"], 0)


    # --------------------------
    # Results Calculation Tests
    # --------------------------
    
    @patch("app.get_skill_levels_and_importance")
    def test_calculate_results_full_match(self, mock_data):
        # If a user meets or exceeds all O*NET levels, compatibility score should be 100%
        
        mock_data.return_value = [
            {"skill_name": "Python", "onet_level": 3, "onet_importance": 5}
        ]

        ranked, matched, improve, score = calculate_results(
            "123", {"Python": 5}
        )

        self.assertEqual(score, 100)
        self.assertEqual(matched, ["Python"])
        self.assertEqual(improve, [])

    @patch("app.get_skill_levels_and_importance")
    def test_calculate_results_partial(self, mock_data):
        # If user partially matches, compatibility score should reflect ratio of matched skills
        
        mock_data.return_value = [
            {"skill_name": "Python", "onet_level": 5, "onet_importance": 5},
            {"skill_name": "SQL", "onet_level": 5, "onet_importance": 5}
        ]

        ranked, matched, improve, score = calculate_results(
            "123", {"Python": 5, "SQL": 1}
        )

        self.assertEqual(score, 50)
        self.assertIn("Python", matched)
        self.assertIn("SQL", improve)

    def test_calculate_results_empty(self):
        # Empty user ratings should return 0% score
        
        ranked, matched, improve, score = calculate_results("123", {})

        self.assertEqual(score, 0)
        self.assertEqual(ranked, [])


    # ----------------------
    # Core Logic Edge Cases
    # ----------------------

    def test_rank_skill_gaps_empty_input(self):
        # Empty skill data should return empty list
        result = rank_skill_gaps([], {})
        self.assertEqual(result, [])


    def test_calculate_results_no_skill(self):
        # Calculate results with empty user ratings and no skills
        ranked, matched, improve, score = calculate_results("123", {})

        self.assertEqual(score, 0)
        self.assertEqual(ranked, [])
        self.assertEqual(matched, [])
        self.assertEqual(improve, [])

# ----------------------
# Database Access Tests
# ----------------------

class TalentTrailDatabaseAccessTests(unittest.TestCase):
#Tests for database access functions
    
    # ------------------
    # get_careers Tests
    # ------------------

    @patch("app.sqlite3.connect")
    def test_get_careers_returns_list(self, mock_connect):
        # Verify get_careers returns a list of tuples with code and title
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.fetchall.return_value = [
            ("13-2011.00", "Accountants and Auditors")
        ]

        careers = get_careers()
        self.assertIsInstance(careers, list)
        self.assertEqual(careers[0], ("13-2011.00", "Accountants and Auditors"))
        
    # -----------------
    # get_skills Tests
    # -----------------

    @patch("app.sqlite3.connect")
    def test_get_skills_with_valid_code(self, mock_connect):
        # Returns top 10 skills for valid career code
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.fetchall.return_value = [("Python", 5, "desc")]

        skills = get_skills("123")
        self.assertIsInstance(skills, list)
        self.assertEqual(skills[0][0], "Python")

    def test_get_skills_with_no_code(self):
        # Returns empty list when no career code is provided
        self.assertEqual(get_skills(None), [])

    # ----------------------
    # get_career_name Tests
    # ----------------------

    @patch("app.sqlite3.connect")
    def test_get_career_name_found(self, mock_connect):
        # Returns correct career name for a known code
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = ("Engineer",)
        mock_connect.return_value.cursor.return_value = mock_cursor
        
        name = get_career_name("123")
        self.assertEqual(name, "Engineer")

    @patch("app.sqlite3.connect")
    def test_get_career_name_not_found(self, mock_connect):
        # Returns 'Unknown Career' for unknown code
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.fetchone.return_value = None

        name = get_career_name("999")
        self.assertEqual(name, "Unknown Career")
        
# -------------------------
# Database Edge Case Tests
# -------------------------

class TalentTrailDatabaseTests(unittest.TestCase):

    def test_get_skills_no_input(self):
        skills = get_skills(None)
        self.assertEqual(skills, [])

    @patch("app.sqlite3.connect")
    def test_get_skills_db_failure(self, mock_connect):
        # Simulate a db connect error

        mock_connect.side_effect = Exception("DB connection failed")
        with self.assertRaises(Exception):
            get_skills("123")

# ----------------------------------
# End to End Career Quiz Flow Tests
# ----------------------------------

class TalentTrailE2ETests(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    @patch("app.get_skills")
    @patch("app.get_career_name")
    @patch("app.calculate_results")
    def test_full_quiz_flow_mock_data(self, mock_calc, mock_name, mock_skills):
        # Mock skills and career name for test
        mock_skills.return_value = [("Python", 5, "desc"), ("SQL", 4, "desc")]
        mock_name.return_value = "Engineer"
        mock_calc.return_value = ([], ["Python", "SQL"], [], 100)
        
        # Landing Page
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Talent Trail", response.data)

        # Career Selection
        response = self.client.get("/careers")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Select a Career", response.data)
        
        # Survey Page with Selected Career
        response = self.client.get("/careers/survey?career=123")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Skills Survey", response.data)
        self.assertIn(b"Engineer", response.data)

        # Survey to Results Page
        survey_data = {"career_code": "123", "rating_0": "5", "rating_1" : "4"}
        response = self.client.post("/careers/survey/results", data=survey_data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Career Compatibility Results", response.data)
        self.assertIn(b"Engineer", response.data)
        self.assertIn(b"Python", response.data)
        self.assertIn(b"SQL", response.data)


# -------------------
# Run Tests
# -------------------

if __name__ == "__main__":
    unittest.main()

