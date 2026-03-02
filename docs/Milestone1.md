# Milestone 1: Project Proposal

## **Talent Trail**

### Team Information
- **Team Number:** 1
- **Team Name:** Algorithm Alliance 

#### Team Members
- **Lisa Wilder** (GitHub: `Wilder407`, Email: Lisa.Wilder@colorado.edu)
- **Kassidy Flick** (GitHub: `kflick3r`, Email: kassidy.flick@colorado.edu)
- **Mark Olmscheid** (GitHub: `Olmscheid`, Email: Mark.Olmscheid@colorado.edu)
- **Sarah Suliman** (GitHub: `sssuliman`, Email: Sarah.Suliman@colorado.edu)

#### Scheduled Weekly Team Meeting
**Sunday at 10 a.m. (MST) via Zoom**
  
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
2. User selects career from a dropdown
3. Backend retrieves:
    - Career description
    - Required skills list
4. User completes survey (Yes/No)
5. Backend:
    - Calculates match %
    - Identifies missing skills
6. Results page displays:
    - Career description
    - Match percentage
    - Missing skills
    - Selected skills users have
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
    
## Project Tracking Software Link:
Weekly Agile/SCRUM meetings. Jira is organized by Milestone and Userstories.


**Jira** (Trello):
https://algorithm-alliance.atlassian.net/jira/core/projects/T1C/board?filter=&groupBy=status&atlOrigin=eyJpIjoiZTUxNjQ0MDc4ZTE3NDExY2IxYTI4ZmFiZDhiOGQ1MzIiLCJwIjoiaiJ9

---

## Potential Add-on Features:
| Feature | Description | Benefit |
|---------|-------------|--------|
| 1–5 Skill Rating | Replace Yes/No survey with a 1–5 scale | Provides more nuanced insight into skill mastery |
| Skill Categories | Organize skills into Technical, Soft Skills, Education, Experience | Enables a more detailed and meaningful analysis |
| Career Progress Tracking | Track user progress over multiple sessions | Supports long-term skill development and repeated assessments |
| Multi-Career Comparison | Compare user skills across multiple careers | Helps users explore alternative career paths |
| Skill Weighting | Weight skills by importance for career | Improves match accuracy and career relevance |

---

## Potential Risks & Edge Cases

| Risk / Edge Case | Description | Mitigation Strategy |
|-----------------|-------------|------------------|
| Survey Overload | Some careers have many skills; survey may be overwhelming | Potentially limit 10–20 key skills per career? |
| O*NET Data Gaps | Missing or outdated data for certain careers | Use a subset of careers for MVP? |
| PDF Generation Errors | Large reports may fail or break layout | Test PDF generation thoroughly; provide fallback to simple HTML export? |
| Misinterpretation of Match % | Users may assume match % guarantees career success | Include disclaimer: “Based on self-assessment and O*NET data” |
| Trie Search Edge Cases | Typing errors may prevent career selection | Implement fuzzy matching and autocomplete suggestions |