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
        - Uses mock data to avoid DB dependencey

Usage: 
    python -m unittest test_app.py
"""

import unittest

from unittest.mock import patch

from app import app, rank_skill_gaps, calculate_results, get_skills

# -------------------
# Test Flask Routes
# -------------------

class TalentTrailRouteTests(unittest.TestCase):
    
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    
    # Landing Page Tests
    def test_landing_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<html', response.data)

    
    # Career Selection Page Tests using patch 
    @patch("app.get_careers")
    def test_career_selection_page(self, mock_careers):
        mock_careers.return_value = [
            ("1", "Engineer"),
            ("2", "Doctor")
        ]
        
        response = self.client.get('/careers')
        
        self.assertEqual(response.status_code, 200)

        #Check if dropdownn exists
        self.assertIn(b'<select', response.data)

        #Check if Mock Careers Appear
        self.assertIn(b'Engineer', response.data)
        self.assertIn(b'Doctor', response.data)
        

    # Survey Page Tests
    def test_survey_page_requires_career_selection(self):
        response = self.client.get('/careers/survey')
        
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Error: No career selected', response.data)


    @patch("app.get_skills")
    @patch("app.get_career_name")
    def test_survey_page_with_valid_career(self, mock_name, mock_skills):
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


    # Results Page Tests
    @patch("app.get_skills")
    @patch("app.get_career_name")
    @patch("app.calculate_results")
    def test_results_route(self, mock_calc, mock_name, mock_skills):
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
        response = self.client.post('/careers/survey/results', data={})

        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Error: No career code submitted.', response.data)

        
# -------------------
# Test Core Logic
# -------------------

    def test_rank_skill_gaps_basic(self):
        skill_data = [
            {"skill_name": "Python", "onet_level": 5, "onet_importance": 5}
        ]

        user = {"Python": 3}

        result = rank_skill_gap(skill_data, user)

        self.assertEqual(result[0]["gap"], 2)
        self.assertGreater([0]["weighted_gap"], 0)