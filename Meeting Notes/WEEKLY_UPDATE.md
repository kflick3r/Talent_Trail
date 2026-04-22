# WEEKLY_STATUS.md
## Project Milestone 3: Weekly Status Report

**Project:** Talent Trail  
**Team Number:** 1  
**Team Name:** Algorithm Alliance  
**Weekly Note Taker:** Mark Olmscheid  

---

## Overview
This document captures the **weekly status** of the Talent Trail project for the specified reporting period.  
It is intended to provide a concise snapshot of progress, plans, and risks, and will be updated weekly throughout the project.

This weekly status format is designed to:
- Track ongoing progress over time
- Surface risks and blockers early
- Provide accountability for individual contributions
- Supplement the project management tool used by the team

---

## Project Management Snapshot
The team is using a shared **Jira board** to manage tasks and sprint progress.

At the time of this report:

- Tasks continue to be aligned to user stories  
- Work is distributed across frontend, backend, database, and algorithm development  
- The team added a **Wednesday Discord check-in** to improve coordination and maintain momentum between meetings  
- Team members are beginning to align implementation work across connected pages and features  

---

## Reporting Period
**Week:** 6  
**Meeting Held:** Yes   
**Meeting Date:**  3/1/2026  
**Meeting Duration:** 60 minutes  
**Meeting Format:** Zoom  


### Progress Since Last Week

This week, the team focused on organizing project requirements, refining the MVP, exploring the technical structure of the data.

Major Progress Items:

- User stories were cleaned up and completed in preparation for effort-level voting  
- Jira tasks were added to correspond with user stories  
- ONET data sources were reviewed and core datasets were identified for the MVP  
- Research was conducted on SQL data storage and how data will integrate into the full-stack application  


### Completed Tasks

- Cleaned up and finalized user stories for effort voting  
- Added Jira tasks tied to each user story  
- Researched trie tree logic and drafted initial pseudocode for a search bar prototype  
- Explored ONET data structure and identified likely core datasets for the MVP  
- Began drafting an overview of MVP data inputs and requirements  
- Researched how SQL data storage can support full-stack integration and user input storage  
- Discussions about website layout and backend structure 


### Planned Tasks for Next Week 
- Create a static dropdown menu connected to career selections  
- Continue building the MVP data-definition and requirements summary  
- Start drafting general algorithm/pseudocode for weighting skills, education, and experience  
- Explore data sorting and conditional formatting to support dropdown filtering and improve the user experience  


### Blockers and Issues
No major technical blockers were encountered this week.

- The team still needs firmer alignment on final MVP deliverables  
- The team may need an additional communication checkpoint, such as a midweek Discord check-in, to stay aligned  


## Risks and Mitigation

**Identified Risk:** Unclear MVP scope  
- *Mitigation:* Finalize MVP deliverables as a group and align technical work directly to that narrowed scope


### Team Reflection

Overall the team has had great progress and communication this week, however, there is an opportunity to align on MVP deliverables and ensure that all technical work is directly supporting those deliverables.


### Individual Contributions This Week
- **Kassidy:** Cleaned up and completed user stories for effort-level voting, added corresponding tasks to Jira, organized the repository with additional folders, and researched trie tree logic while drafting early search bar pseudocode.  
- **Mark:** Explored and identified ONET data for the project’s core datasets, investigated the structure of the data, and began outlining MVP data-input requirements and overall technical needs.  
- **Lisa:** Researched how SQL stores data and how it integrates into a full-stack application, then applied that research to team conversations around layout, data requests, and user input storage.  
- **Sarah:** : Designed initial front-end layout ideas and discussed ideas on how to structure the website based on the MVP deliverables.

---

## Reporting Period
**Week:** 7   
**Meeting Held:** Yes   
**Meeting Date:** 3/8/2026   
**Meeting Duration:** 60 minutes   
**Meeting Format:** Zoom   

### Progress Since Last Week

This week, the team moved from planning and technical exploration into early implementation work across the MVP.

Major Progress Items:

- A weighting algorithm for comparing skills and education was developed and documented in a markdown file  
- A rough landing page template was created for the career selection page  
- SQL data was consolidated into a single database structure  
- The database was connected to the webpage so users can launch the site and select careers  
- Initial design and visual style work continued through mockups  
- Milestone 4 documentation work was started  


### Completed Tasks

- Developed the weighting algorithm for selecting and comparing skills and education  
- Uploaded algorithm documentation in markdown format  
- Created a rough landing page template in GitHub for the career selection page  
- Built a barebones Python test for the webpage workflow  
- Combined SQL data into a single database  
- Connected the database to the webpage  
- Enabled webpage launch and career selection functionality  
- Created initial design mockups and started visual style planning  
- Worked on Milestone 4 page test documentation  


### Planned Tasks for Next Week

- Continue implementing Python code for MVP functionality  
- Refine the homepage so it better matches the intended final design  
- Add descriptions and improve homepage implementation  
- Begin implementing the next connected pages  
- Set up generation and structure for the survey page  
- Identify how career selections will connect to the skills-ranking page  
- Finalize Milestone 4 deliverables  
- Create mockups for all five planned pages  
- Begin integrating visual design into the working website  
- Continue coordinating how the algorithm will use user skill choices and ranking inputs  


### Blockers and Issues

Current blockers and issues include:

- Some uncertainty remains around the structure of the page following career selection  
- Database connection points and storage flow still need further clarification  
- Several team members noted time constraints this week  
- Design implementation is still in an exploratory phase and not yet fully mapped into development  


### Risks and Mitigation

**Identified Risk:** Disconnect between page flow, database logic, and algorithm inputs  
- *Mitigation:* Coordinate more tightly across frontend, backend, and algorithm responsibilities, with clearer handoffs between career selection, survey input, and output generation

**Identified Risk:** Reduced availability this week due to outside commitments  
- *Mitigation:* Added a Wednesday Discord check-in and narrowed focus to core MVP implementation tasks

**Identified Risk:** Design work may outpace implementation planning  
- *Mitigation:* Sarah will create mockups for all key pages so Kassidy and Lisa can build against a clearer visual target


### Team Reflection

This week showed meaningful progress toward a working MVP, especially in moving from planning into actual implementation. The team now has early webpage functionality, a connected database, and a documented algorithm direction. At the same time, the project still needs stronger alignment between page structure, user flow, design implementation, and backend logic. The added Wednesday Discord check-in should help the team stay coordinated during the week and reduce ambiguity as development continues.


### Individual Contributions This Week

- **Kassidy:** Created a rough landing page template for the career selection page, built a barebones Python test, consolidated the SQL data into one database, connected that database to the webpage, and enabled webpage launch with career selection functionality.  
- **Mark:** Developed the weighting algorithm for selecting and comparing skills and education and uploaded the algorithm documentation in a markdown file.  
- **Lisa:** Worked on identifying the connection points between databases and began thinking through how the database will store information and support transitions from career selection to the skills page.  
- **Sarah:** Picked the color scheme, design direction, and visual style, created a mockup, and worked on Milestone 4 page test documentation.  


### Team Focus / Role Alignment

Current division of work is shaping up as follows:

- **Kassidy:** Backbone development and dropdown / skills-page structure  
- **Lisa:** Connecting results and user choices across pages  
- **Mark:** Developing the algorithm based on user variables and skills choices  
- **Sarah:** Developing HTML / landing page styling and broader visual design  


### Planned Frontend Pages

The team identified the following target frontend pages for the MVP:

1. **Landing Page**  
   - About page  
   - High-level overview  
   - Button leading to the selection page  

2. **Homepage / Career Search Page**  
   - Career search functionality  
   - Button connecting to the skills-ranking page  

3. **Skills Page**  
   - Ranking and input page  

4. **Compatibility Page**  
   - Output/results page  

5. **Contact Page / Project GitHub Page**  
   - Contact information and repository reference  

---

## Reporting Period
**Week:** 9   
**Meeting Held:** Yes   
**Meeting Date:** 3/22/2026   
**Meeting Duration:** 30 minutes   
**Meeting Format:** Zoom   


### Progress Since Last Week

This week, the team continued building the MVP by improving documentation, frontend structure, and planning for backend connectivity.

Major progress this week included:

- Created and uploaded an entity relationship diagram to the project documents  
- Added documentation for database structure, including a table for scale reference  
- Got the survey page to load  
- Created the HTML for the results page  
- Continued shared frontend and CSS work and updated the landing page to better match the mockup  
- Continued planning backend work for comparing user inputs to the career database  


### Planned Tasks for Next Week

- Work on Flask connectivity for the HTML pages  
- Determine how the application will connect to the database and present output to the user  
- Continue working on the backend algorithm for comparing user inputs to the career database  
- Add the About page
- Write tests for the current pages and routes  
- Continue updating and refining the frontend  


### Blockers and Issues

Current blockers and issues include:

- CSS pathing is currently hardcoded  
- The team still needs to determine a standardized path for how to run the app  
- Progress on backend algorithm work over the last couple of weeks was slowed by wedding and work commitments  


### Individual Contributions This Week

- **Lisa:** Reviewed how the data connects across the project, created and uploaded the entity relationship diagram, added documentation, and added the scale reference table.  
- **Kassidy:** Worked on getting pages to appear, got the survey page to load, and created the HTML for the results page.  
- **Sarah:** Started creating the shared frontend and CSS, continued designing the page, and updated the landing page to match the mockup more closely.  
- **Mark:** Continued planning backend work for the algorithm that compares user inputs to the career database.  


### Individual Plans for Next Week

- **Lisa:** Work on Flask connectivity for HTML and determine how the app will connect to the database and present output.  
- **Kassidy:** Add the About page and write tests.  
- **Sarah:** Continue updating and refining the frontend.  
- **Mark:** Continue working on the backend algorithm for comparing user inputs to the career database.  

---

**Week:** 10   
**Meeting Held:** Yes    
**Meeting Date:** 3/29/2026   
**Meeting Duration:** 30 minutes   
**Meeting Format:** Zoom   

### Progress Since Last Week

This week, the team made progress connecting frontend pages to backend functionality, improving documentation, and continuing milestone support work.

### Major Progress Items

- Connected survey responses to the backend so the results page now displays:
  - selected career
  - compatibility score
  - matched skills
  - skills to improve
- Fixed routing issues in JupyterHub so navigation works between the landing page, career selection page, survey page, and results page
- Continued applying shared CSS and updated the landing page styling to better match the mockups
- Continued development of the comparison algorithm and milestone support work
- Began work on unit testing and About page content
- Continued database and results-page work, including support for storing user responses and milestone documentation

### Planned Tasks for Next Week

- Finish applying CSS across the career selection, survey, and results pages for a more consistent UI
- Clean up the HTML structure and begin organizing templates
- Explore using template inheritance to reduce repeated code across pages
- Test the comparison algorithm and continue refining its output
- Write/update the About page for the algorithm and project
- Continue unit testing
- Continue results page and PDF-related milestone work

### Blockers and Issues

Current blockers and issues include:

- Routing and static file paths remain challenging in the JupyterHub proxy environment
- CSS and navigation links are not yet fully standardized across the app
- The team is still working through how to consistently handle the JupyterHub/csel proxy setup without duplicating effort

### Individual Contributions This Week

- **Mark:** Pushed updates to the comparison algorithm, updated the weekly status, and continued backend work supporting career-data comparison.
- **Kassidy:** Started unit testing, worked on the About page, and supported Milestone 5 tasks.
- **Lisa:** Worked on the Milestone 5 document, set up the table for user responses, and confirmed response data was being added properly.
- **Sarah:** Implemented the dynamic results page by connecting survey responses to the backend, fixed JupyterHub routing between the main app pages, and continued applying shared CSS and updating the landing page styling.

### Individual Plans for Next Week

- **Mark:** Test the algorithm, write About page content for the algorithm, and continue updating project documentation.
- **Kassidy:** Finish unit testing and continue About page work.
- **Lisa:** Continue work on the results page and PDF-related tasks.
- **Sarah:** Finish applying CSS across remaining pages, clean up the HTML structure, and begin organizing templates with possible template inheritance.

---

## Reporting Period
**Week:** 11   
**Meeting Held:** Yes   
**Meeting Date:** 4/6/2026   
**Meeting Duration:** 45 minutes   
**Meeting Format:** Zoom   


### Progress Since Last Week

This week, the team moved from early implementation work across the MVP to a viable product.

Major Progress Items:

- Unit tests were written and passed
- Design and style has near completion
- Results PDF generation successfully linked


### Completed Tasks

- Tests for Backend routes and database queries written
- Write tests for database and flask routes
- Implement backend PDF generation route
- Implement Consistent Styling Across all Pages
- Dynamically display matched skills and percentage match


### Planned Tasks for Next Week

- Update powerpoint with screenshots and detailed information about the project
- Verify that the information displayed on PDF is desired result
- Connect styling to PDF result HTML page
- Identify if skills can be displayed according to importance instead of first tem
- Implement code to open the PDF in a new page
- Verify end-to-end test continues to work after final changes are implemented


### Blockers and Issues

Current blockers and issues include:

- One team member is experiencing issues loading the PDF module
- Identifying the module for PDF creation locally and on JH was thorough
- Identify how to have data persist through the session and be output to the PDF
- Some team members noted time constraints this week
- Weasyprint PDF module may be causing issue for a team member


### Risks and Mitigation

**Identified Risk:** Virtual environment modules installation concern 
- *Mitigation:* Sarah will review the issue and reach out if persists to seek team support.

**Identified Risk:** Reduced availability this week due to outside commitments  
- *Mitigation:* Continued mid-week discord check-in has proved helpful to keep team on timeline

**Identified Risk:** Scope of final project presentation materials
- *Mitigation:* Plan for strong communication between team members to ensure that the workload is distributed.


### Team Reflection

This week showed meaningful progress toward a working MVP, especially in moving from planning into actual implementation. The team now has early webpage functionality, a connected database, and a documented algorithm direction. At the same time, the project still needs stronger alignment between page structure, user flow, design implementation, and backend logic. The added Wednesday Discord check-in should help the team stay coordinated during the week and reduce ambiguity as development continues.


## Individual Contributions This Week

- **Kassidy:** Created and verified 24 units tests that encompass all aspects of the routes, database and page loading
- **Mark:** Wrote algorithm information for the about page and the unit tests for the algorithm
- **Lisa:** Created the pdf generation flask route and coneccted data throughout a session 
- **Sarah:** Impletemented the CSS across the HTML pages for a fully visualized webpage.

---
