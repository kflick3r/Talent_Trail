# Milestone 8: Final Report

## **Talent Trail**

### Team Information
- **Team Number:** 1
- **Team Name:** Algorithm Alliance

### Project Title
## Talent Trail - A web-app used to evaluate career readiness for a chosen career

#### Team Members
- **Lisa Wilder** (GitHub: `Wilder407`, Email: Lisa.Wilder@colorado.edu)
- **Kassidy Flick** (GitHub: `kflick3r`, Email: kassidy.flick@colorado.edu)
- **Mark Olmscheid** (GitHub: `Olmscheid`, Email: Mark.Olmscheid@colorado.edu)
- **Sarah Suliman** (GitHub: `sssuliman`, Email: Sarah.Suliman@colorado.edu)
  
---

## Required Links:
- **Project Tracker (instructor has access)**: *Jira* https://algorithm-alliance.atlassian.net/jira/core/projects/T1C/board?filter=&groupBy=status&atlOrigin=eyJpIjoiZTUxNjQ0MDc4ZTE3NDExY2IxYTI4ZmFiZDhiOGQ1MzIiLCJwIjoiaiJ9
- **Version Control Repository**: *Github* (public) https://github.com/kflick3r/Talent_Trail
- **Demo Video**: https://drive.google.com/file/d/1WE2Smd3j-kiLPdorW5b4QrEOJeYeEoC-/view?usp=sharing
- **Public Deployment Site**: *Render* https://talent-trail.onrender.com/

---

## Repository Readiness
All team members have verified that their latest work is pushed to the remote repository.

The reposity contains the following required files and assests:

- README.md
- WEEKLY_STATUS.md
- PAGE_TESTING.md
- SQL_TESTING.md
- FINAL_REPORT.md
- Project presentation files from the Presentation Milestone
- Video of demo
- Source code (frontend and backend)
- Test cases (unit and integration)
- Source documentation and auto-generated documentation files

---

## Final Status Report

### What Team 1 completed:
- Working MVP including:
- Career Selection & Skill Retrieval
- Personalized Skill Survey
- Feedback and Guidance based on compatibility score
- Calculates a compatibility score based on if the user meets or exceeds the O*NET baseline
- PDF Report Generation

### What Team 1 was in the middle of completing:
- Retrieving the career description for display on survey and results page. 

### What we planned for the future:
- User login to store survey results
- Incorporate experience and education requirements/preferences into survey
- Trie search or text entry based search to streamline career selection
- Create skill categories to better represent soft versus technical skills
- Display typical education distribution for selected careers

### Known problems and limitations:
- The career list not searchable. 
- The survey is rudimentary making skill gap/compatibility score only relative to the skills presented.

## System Overview

Talent Trail uses a standard three-tier architecture:
- Frontend: HTML/CSS
- Backend: Flask
- Database: SQLite3

The system was designed based on the prior skills and knowledge of the team as well as the curriculum in the course. Team members also researched and implemented module connectivity that supported the MVP. 

## Pages that access database information
- Careers: present survey user with list of available careers
- Survey: Present user with 15 most important skills for the chosen career through a session
- Results: Career Title, skill list

---

## Reflection
This project has been instrumental in leaning to see an idea through to a viable product. As a team, we got first hand experience with agile, version control, frontend, backend, HTML, deployment, testing, and presenting a working product. 

#### **Key Takeaways:**
- Scope control is crucial. Defining the MVP and following it strictly is very important.
- New features can always be added in later.
- Communication is manditory and very important to the project.
- Task ownership and proactivity pays off in the end.

---

## Vision Statement:
Talent Trail is a web-based career exploration tool that helps users evaluate how closely their current skills, education, and experience align with the selected desired career and professional goals. Using occupational data from the O*NET database, Talent Trail generates a personalized gap analysis report to show users their match percentage and what is still needed to achieve potential careers. 
    
---

## Motivation: 
People often struggle to evaluate their skill sets and understand whether they are qualified for their desired career. Figuring out what is needed to reach a dream career can be overwhelming and time-intensive, with conflicting information across the internet. Talent Trail aligns the O*NET database with a user’s information to provide clear, data-driven comparisons. This transforms career planning into a tangible and digestible evaluation. 

---

## Project Risks:
- **Scheduling and Time**: Working with a new team on an asynchronous schedule may limit shared work time. 
- **Prior Experience:** No prior experience in full-stack development.
- **Feature Scope:** Identifying the scope and MVP and sticking with it, rather than letting imagination expand the project scope. 
- **Full-Stack Integration:** Deciding on technologies and languages to use and learn.
- **Expectations:** Individual expectations regarding time and energy spent on the success of the application. 
  
---    

## Mitigation Strategy:
- Survey stakeholders for information needed to develop the application (Office Hours)
- Adapt to learning new strategies and information as needed
- Individual asynchronous learning 
- Finalize database early to implement the sorting algorithm
- Conduct testing early to catch bugs
- Hold an initial, candid conversation about expectations and time commitment
- Communicate weekly via Discord Team Messenger for general conversations, check-ins, and casual questions
- Email major progress and concerns to the team, with Professor Guinn cc'd

---

## MVP Structure/Functional Requirements:
MVP Goal: Deliver a fully functional career gap analysis tool that allows users to select a career, assess their skills, and recieve a personalized report.

**User Flow**
1. User lands on homepage
2. User selects career from searchable dropdown
3. Backend retrieves:
    - Career description
    - Required skills list
4. User completes survey (1–7 scale)
5. Backend:
    - Calculates match percentage
    - Identifies missing skills
6. Results page displays:
    - Match percentage
    - Skills the user possesses
    - Skills that need improvement
    - Button to generate PDF
7. PDF of report is generated and downloaded

---

## Development Method: 
1. Define core user stories and the MVP functional requirements, such as:
   - User selects a career from a dropdown
   - System retrieves career description and required skills from O*NET database
   - User completes a skill, education, and experience survey
   - System Calculates:
       - Match Percentage
       - Missing Skills, Education, and/or Experience
   - System generates results page and downloadable PDF report 
2. Identify the system requirements and tech stack:
   - Backend: Python (Flask)
   - Database: SQL / SQLite?
   - Frontend: HTML/CSS
   - Version Control: Github
   - PDF generation: Python Library (reportlab or HTML-to-PDF)
3. Design database schema for:
    - Careers
    - Skills
    - Education
    - Previous Experience
4. Implement backend API based on functional requirements:
   - Route: Landing Page
   - Route: Career Selection
   - Route: Survey Submission
   - Route: Results Page
   - Route: PDF generation
5. Build frontend views:
   - Landing Page
   - Survey Page
   - Results Page
   - PDF Download Option
6. Integrate frontend and backend components
7. Conduct testing and prepare final presentation and documentation.
  
---

## Future Development Possibilities
| Feature                                      | Description                                                             | Benefit                                                                  |
| -------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Trie Tree Career Selection                   | Replace career selection dropdown with a Trie Tree algorithm            | Faster and more intuitive career search; improves user experience        |
| Skill Categories                             | Organize skills into Technical, Soft Skills, Education, Experience      | Provides a more detailed and meaningful analysis of user skills          |
| Career Progress Tracking                     | Track user progress across multiple sessions                            | Supports long-term skill development and repeated assessments            |
| Multi-Career Comparison                      | Compare user skills across multiple careers                             | Helps users explore alternative career paths and make informed decisions |
| Incorporate Experience & Education           | Include previous work experience and education in compatibility scoring | Produces a more holistic and accurate assessment of career readiness     |
| Education Distribution Visualization         | Display typical education distribution for selected careers             | Helps users understand common career paths and educational requirements  |
| User Accounts & Saved Reports                | Enable login and report saving for multiple sessions                    | Supports long-term tracking and personalized planning                    |


---

## Potential Risks & Edge Cases

| Risk / Edge Case | Description | Possible Mitigation Strategy |
|-----------------|-------------|------------------|
| Survey Overload | Some careers have many skills; survey may be overwhelming | Potentially limit 10–20 key skills per career? |
| O*NET Data Gaps | Missing or outdated data for certain careers | Use a subset of careers for MVP? |
| PDF Generation Errors | Large reports may fail or break layout | Test PDF generation thoroughly; provide fallback to simple HTML export? |
| Misinterpretation of Match % | Users may assume match % guarantees career success | Include disclaimer: “Based on self-assessment and O*NET data” |
