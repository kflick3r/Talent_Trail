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
    
## Development Method: 
1. Define core user stories and the MVP functional requirements, such as:
   - User selects a career form a searchable dropdown (Trie-Based Search)
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
Jira (Trello) https://algorithm-alliance.atlassian.net/jira/core/projects/T1C/board?filter=&groupBy=status&atlOrigin=eyJpIjoiZTUxNjQ0MDc4ZTE3NDExY2IxYTI4ZmFiZDhiOGQ1MzIiLCJwIjoiaiJ9
