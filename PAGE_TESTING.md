# PAGE_TESTING.md

This document defines the **pages** Talent Trail will implement and what is required to (1) render them correctly and (2) test them consistently.

---

## Conventions Used in This Document

### Parameter Types
- Route params: values embedded in the URL path (example: /career/:careerName)
- Query params: values after ? in the URL (example: ?career=backend)
- State params: values passed through navigation state

### Data Types
- API data: data retrieved from backend services
- UI state: temporary interface values such as form inputs or selections
- User input: responses provided in the skills quiz

### Mockups
Each page includes a low-fidelity ASCII mockup representing the layout. These may later be replaced with screenshots from the Figma designs.

---

# 1) Homepage (Career Search)

## Page Title
Homepage

## Page Description
Purpose: Allow users to search for a career and view a short description of the role along with the required skills. The page also allows users to begin a skills quiz to determine their compatibility with the selected career.

**Mockup (low-fidelity):**
```
+------------------------------------------------------+
| Talent Trail                                         |
| Discover careers that match your skills              |
|------------------------------------------------------|
|  [ Search Career __________________ ] [Search]       |
|                                                      |
| Job Description                                      |
| Back-end developers build and maintain server apps   |
|                                                      |
| Required Skills                                      |
| • Python                                             |
| • SQL                                                |
| • React                                              |
|                                                      |
|                    [ Take Quiz ]                     |
+------------------------------------------------------+
```

## Parameters Needed for the Page
	•	Route params: none
	•	Query params: optional ?career=name

## Data Needed to Render the Page
	•	Career title
	•	Job description
	•	Required skills list
	•	UI state for search input

## Link Destinations for the Page
	•	Take Quiz → /quiz
	•	About → /about
	•	Contact → /contact
	•	GitHub → external repository

## Tests for Verifying Rendering of the Page
	1.	Verify the page title renders correctly.
	2.	Verify the search input accepts text.
	3.	Verify clicking the search button displays a career description.
	4.	Verify required skills display correctly.
	5.	Verify the “Take Quiz” button navigates to the quiz page.

---

# 2) Skills Quiz Page

## Page Title
Back-end Developer Skills Quiz

## Page Description
Purpose: Collect information about a user’s experience with key technologies related to the selected career. The user answers yes or no questions about their familiarity with Python, SQL, and React. The user also selects their education level from a dropdown menu.

**Mockup (low-fidelity):**
```
+------------------------------------------------------+
| Talent Trail                                         |
| Back-end Developer Skills Quiz                       |
|------------------------------------------------------|
| Do you have experience with the following?           |
|                                                      |
| Python        Yes ( )   No ( )                       |
| SQL           Yes ( )   No ( )                       |
| React         Yes ( )   No ( )                       |
|                                                      |
| Education Level                                      |
| [ Bachelor's Degree ▼ ]                              |
|                                                      |
| [ Return to Homepage ]    [ Submit Quiz ]            |
+------------------------------------------------------+
```

## Parameters Needed for the Page
	•	Route params: none
	•	Query params: optional ?career=name

## Data Needed to Render the Page
	•	Career name
	•	List of skill questions
	•	Education level options
	•	User responses

## Link Destinations for the Page
	•	Submit Quiz → /results
	•	Return to Homepage → /

## Tests for Verifying Rendering of the Page
	1.	Verify all skill questions render correctly.
	2.	Verify users can select Yes or No options.
	3.	Verify the education dropdown works properly.
	4.	Verify the Submit Quiz button processes responses.
	5.	Verify the Return to Homepage button navigates correctly.

---

# 3) Career Compatibility Results Page

## Page Title
Career Compatibility Results

## Page Description
Purpose: Display the user’s compatibility score for a selected career based on their quiz responses. The page also highlights the skills the user already possesses and the skills they should improve.

**Mockup (low-fidelity):**
```
+------------------------------------------------------+
| Talent Trail                                         |
| Career Compatibility Results                         |
|------------------------------------------------------|
| Career: Back-end Developer                           |
| Compatibility Score: 78%                             |
|                                                      |
| Matched Skills          Skills to Improve            |
| • Python                • React                      |
| • SQL                                                |
|                                                      |
| Recommendation                                       |
| Learning React will increase your compatibility      |
| with back-end developer roles.                       |
|                                                      |
| [ Return to Quiz ]     [ Homepage ]                  |
+------------------------------------------------------+
```

## Parameters Needed for the Page
	•	Route params: none
	•	Query params: optional ?career=name

## Data Needed to Render the Page
	•	Career title
	•	Compatibility score
	•	Matched skills list
	•	Missing skills list
	•	Recommendation text

## Link Destinations for the Page
	•	Return to Quiz → /quiz
	•	Homepage → /

## Tests for Verifying Rendering of the Page
	1.	Verify compatibility score renders correctly.
	2.	Verify matched skills list displays correctly.
	3.	Verify skills to improve are displayed.
	4.	Verify recommendation text appears.
	5.	Verify navigation buttons function correctly.

---

# 4) About Page

## Page Title
About Talent Trail

## Page Description
Purpose: Provide information about the Talent Trail project and its goal of helping users discover careers that align with their current skills.

**Mockup (low-fidelity):**
```
+------------------------------------------------------+
| Talent Trail                                         |
| About                                                |
|------------------------------------------------------|
| Talent Trail helps users discover careers            |
| that match their existing skills and identify        |
| skills they should develop to improve compatibility. |
|                                                      |
| The platform provides career descriptions,           |
| skill quizzes, and recommendations for improvement.  |
|                                                      |
| [ Back to Homepage ]                                 |
+------------------------------------------------------+
```

## Parameters Needed for the Page
	•	Route params: none
	•	Query params: none

## Data Needed to Render the Page
	•	Project description
	•	Platform overview text

## Link Destinations for the Page
	•	Homepage → /

### Tests for Verifying Rendering of the Page
	1.	Verify the page title displays.
	2.	Verify the project description loads.
	3.	Verify the navigation button returns to the homepage.

---

# 5) Contact Page

## Page Title
Contact

## Page Description
Purpose: Provide users with ways to contact the project team or access the project repository.

**Mockup (low-fidelity):**
```
+------------------------------------------------------+
| Talent Trail                                         |
| Contact                                              |
|------------------------------------------------------|
| For questions or feedback about Talent Trail:        |
|                                                      |
| Email: team@talenttrail.com                          |
| GitHub Repository:                                   |
| https://github.com/...                               |
|                                                      |
| [ Return to Homepage ]                               |
+------------------------------------------------------+
```
## Parameters Needed for the Page
	•	Route params: none
	•	Query params: none

## Data Needed to Render the Page
	•	Contact email
	•	GitHub repository link

## Link Destinations for the Page
	•	Homepage → /
	•	GitHub Repository → external link

## Tests for Verifying Rendering of the Page
	1.	Verify contact information displays correctly.
	2.	Verify the GitHub link opens correctly.
	3.	Verify the homepage navigation link functions properly.




