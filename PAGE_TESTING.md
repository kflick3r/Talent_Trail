# PAGE_TESTING.md

This document defines the **pages** Talent Trail will implement and what is required to (1) render them correctly and (2) test them consistently.

At least **5 independent pages** are included below.

---

## Conventions Used in This Document

### Parameter Types
- **Route params**: values embedded in the URL path (example: `/career/:careerName`)
- **Query params**: values after `?` in the URL (example: `?career=backend`)
- **State params**: values passed through navigation state

### Data Types
- **API data**: data retrieved from backend services
- **UI state**: temporary interface values such as form inputs or selections
- **User input**: responses provided in the skills quiz

### Mockups
Each page includes a **low-fidelity mockup** (ASCII wireframe). These may later be replaced with screenshots from the Figma designs.

---

# 1) Landing Page

## Page Title
Landing Page

## Page Description
Purpose: Introduce Talent Trail, explain what the platform does, and show users how to use the site before they move into the career selection flow.

**Mockup (low-fidelity):**
```
------------------------------------------------------------
                         Talent Trail
              Discover careers that match your skills
------------------------------------------------------------

About

Talent Trail is a web-based career exploration tool that
helps users discover careers that match their current
skills. The application compares a user’s abilities with
industry requirements and generates a compatibility report.

------------------------------------------------------------

How to Use

1. Search for a career you are interested in.
2. Take the skills quiz for that career.
3. View your compatibility score and skill gaps.
4. Review recommended skills to improve.

------------------------------------------------------------

                  [ Start Career Search ]

------------------------------------------------------------
About | Contact | GitHub
------------------------------------------------------------
```

## Parameters Needed for the Page
- Route params: none
- Query params: none

## Data Needed to Render the Page
- Static site title
- Tagline
- About section text
- How-to-use steps
- Navigation links

## Link Destinations for the Page
- **Start Career Search** → `/search`
- **About** → `/`
- **Contact** → `/contact`
- **GitHub** → external repository link

## Tests for Verifying Rendering of the Page
1. **Renders key UI elements**
   - Site title displays
   - Tagline displays
   - About section displays
   - How to Use section displays
2. **Button navigation**
   - Clicking "Start Career Search" navigates to the search page
3. **Footer links**
   - About, Contact, and GitHub links render and are clickable

---

# 2) Search Page

## Page Title
Search Page

## Page Description
Purpose: Allow users to choose a career from a dropdown menu and continue to the quiz for that selected career.

**Mockup (low-fidelity):**
```
------------------------------------------------------------
                         Talent Trail
------------------------------------------------------------

Select a Career

[ Select Career ▼ ]

Example Careers

• Back-end Developer
• Front-end Developer
• Data Analyst
• Software Engineer

------------------------------------------------------------

                 [ Continue to Quiz ]

------------------------------------------------------------
About | Contact | GitHub
------------------------------------------------------------
```

## Parameters Needed for the Page
- Route params: none
- Query params: optional `?career=name`

## Data Needed to Render the Page
- Career dropdown options
- Selected career value
- Continue button state

## Link Destinations for the Page
- **Continue to Quiz** → `/quiz`
- **About** → `/`
- **Contact** → `/contact`
- **GitHub** → external repository link

## Tests for Verifying Rendering of the Page
1. **Dropdown renders**
   - Career dropdown is visible
   - Career options load correctly
2. **Selection behavior**
   - User can select one career from the dropdown
3. **Continue flow**
   - Clicking "Continue to Quiz" after selecting a career navigates to the quiz page
4. **Footer links**
   - About, Contact, and GitHub links render correctly

---

# 3) Quiz Page

## Page Title
Quiz Page

## Page Description
Purpose: Let users rate their experience with required skills and choose their education level so Talent Trail can calculate compatibility with the selected career.

**Mockup (low-fidelity):**
```
------------------------------------------------------------
                         Talent Trail
------------------------------------------------------------

Back-end Developer Skills Quiz

Rate your experience with the following skills
using a scale from 0–7.

0 = No experience
7 = Expert level

------------------------------------------------------------

Python           0 1 2 3 4 5 6 7
SQL              0 1 2 3 4 5 6 7
React            0 1 2 3 4 5 6 7

------------------------------------------------------------

Education Level

[ Bachelor's Degree ▼ ]

------------------------------------------------------------

           [ Return to Homepage ]   [ Submit Quiz ]

------------------------------------------------------------
About | Contact | GitHub
------------------------------------------------------------
```

## Parameters Needed for the Page
- Route params: none
- Query params: optional `?career=name`
- State params: selected career passed from the search page

## Data Needed to Render the Page
- Career name
- Skill list
- Ranking scale values (0–7)
- Education dropdown options
- User-selected responses

## Link Destinations for the Page
- **Submit Quiz** → `/results`
- **Return to Homepage** → `/`
- **About** → `/`
- **Contact** → `/contact`
- **GitHub** → external repository link

## Tests for Verifying Rendering of the Page
1. **Quiz content renders**
   - Career title displays
   - Skill rows display
   - 0–7 rating scale displays
2. **Input behavior**
   - User can select a value for each skill
   - User can choose an education level
3. **Submit flow**
   - Clicking "Submit Quiz" navigates to the results page
4. **Return flow**
   - Clicking "Return to Homepage" navigates to the landing page
5. **Footer links**
   - About, Contact, and GitHub links render correctly

---

# 4) Results Page

## Page Title
Results Page

## Page Description
Purpose: Display the user’s compatibility score, matched skills, missing skills, and feedback after the quiz is submitted.

**Mockup (low-fidelity):**
```
------------------------------------------------------------
                         Talent Trail
------------------------------------------------------------

Career Compatibility Results

Career
Back-end Developer

Compatibility Score
78%

------------------------------------------------------------

Matched Skills

• Python
• SQL

------------------------------------------------------------

Skills to Improve

• React

------------------------------------------------------------

Feedback

Learning React will increase your compatibility with
back-end developer roles.

------------------------------------------------------------

           [ Return to Quiz ]   [ Homepage ]

------------------------------------------------------------
About | Contact | GitHub
------------------------------------------------------------
```

## Parameters Needed for the Page
- Route params: none
- Query params: optional `?career=name`
- State params: quiz responses and selected career

## Data Needed to Render the Page
- Career title
- Compatibility score
- Matched skills list
- Missing skills list
- Feedback message

## Link Destinations for the Page
- **Return to Quiz** → `/quiz`
- **Homepage** → `/`
- **About** → `/`
- **Contact** → `/contact`
- **GitHub** → external repository link

## Tests for Verifying Rendering of the Page
1. **Results content renders**
   - Career title displays
   - Compatibility score displays
   - Matched skills section displays
   - Skills to Improve section displays
   - Feedback section displays
2. **Navigation buttons**
   - Return to Quiz button navigates correctly
   - Homepage button navigates correctly
3. **Footer links**
   - About, Contact, and GitHub links render correctly

---

# 5) Contact Page

## Page Title
Contact Page

## Page Description
Purpose: Provide team member contact information and a link to the project GitHub repository.

**Mockup (low-fidelity):**
```
------------------------------------------------------------
                         Talent Trail
                         Contact Us
------------------------------------------------------------

Team Members

• Lisa Wilder (GitHub: Wilder407, Email: Lisa.Wilder@colorado.edu)
• Kassidy Flick (GitHub: kflick3r, Email: kassidy.flick@colorado.edu)
• Mark Olmscheid (GitHub: Olmscheid, Email: Mark.Olmscheid@colorado.edu)
• Sarah Suliman (GitHub: sssuliman, Email: Sarah.Suliman@colorado.edu)

------------------------------------------------------------

Project Repository

https://github.com/kflick3r/Talent_Trail

------------------------------------------------------------

                 [ Return to Homepage ]

------------------------------------------------------------
About | Contact | GitHub
------------------------------------------------------------
```

## Parameters Needed for the Page
- Route params: none
- Query params: none

## Data Needed to Render the Page
- Team member names
- Team member GitHub usernames
- Team member email addresses
- GitHub repository URL

## Link Destinations for the Page
- **Return to Homepage** → `/`
- **About** → `/`
- **Contact** → `/contact`
- **GitHub** → external repository link

## Tests for Verifying Rendering of the Page
1. **Contact content renders**
   - Team member list displays
   - Repository link displays
2. **Navigation button**
   - Return to Homepage button navigates correctly
3. **Footer links**
   - About, Contact, and GitHub links render correctly


