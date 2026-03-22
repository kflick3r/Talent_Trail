# test_app.py
# 
# Purpose: Unit tests for the app.py file. Testing flask routes and database functions. 
#
# Usage: python -m unittest test_app.py

import unittest

from app import app, get_careers, get_skills, get_career_name

# -------------------
# Test Flask Routes
# -------------------

class TalentTrailRouteTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Landing Page Tests
    def test_landing_page(self):
        reponse = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Talent Trail', response.data)

    # Career Selection Page Tests
    def test_career_selection(self):
        reponse = self.app.get('/careers')
        self.assertEqual(response.status_code, 200)

        # Check for drop down
        self.assertIn(b'<select', response.data)
        # Sample Careers
        sample_careers = [b'Accountants and Auditors', b'Actors', b'Actuaries']
        self.assertTrue(any(career in response.data for career in sample_careers))

    # Survey Page Tests
    def test_survey_page_requires_career_selection(self):
        response = self.app.get('/careers/survey')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Error: No career selected', response.data)

    def test_survey_page_with_valid_career(self):
        sample_code = '13-2011.00'  # Accountants and Auditors
        response = self.app.get(f'/careers/survey?career={sample_code}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Accountants and Auditors', response.data)

        # Check that the survey page contains the career name
        career_name = get_career_name(sample_code)
        self.assertIn(career_name.encode(), response.data)

        # Check that the submit button exists
        self.assertIn(b'<button type="submit">Submit Survey</button>', response.data)


    def test_survey_page_radio_buttons(self):
        sample_code = '13-2011.00'  # Accountants and Auditors
        response = self.app.get(f'/careers/survey?career={sample_code}')

        # Check that radio button exists for at least the first skill
        self.assertIn(b'type="radio"', response.data)

        