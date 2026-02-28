# Talent Trail User Story Cards
<details>
<summary><strong>Algorithm Alliance - Team 1</strong></summary>

<p><strong>Meeting Time:</strong> Sunday @ 10:00 AM</p>

<hr>

<p><strong>Team Members:</strong></p>
<ul>
    <li>Sarah Suliman</li>
    <li>Kassidy Flick</li>
    <li>Mark Olmscheid</li>
    <li>Lisa Wilder</li>
</ul>

</details>

---
#### User Story 1 (Mark) [O*NET Data Storage]
**As a:** back-end developer,  
**I want:** the O*NET data to be organized and stored  
**So that:**  it can be queried by the front end and the roadmap/algorithm can run against a consistent data model.  

##### Effort
Level	:   5

##### Acceptance Criteria
Given: O*NET data has successfully been identified/stored  
When: the front end queries the needed data  
Then: the data is pulled correctly and displayed  
    AND it supports career queries and algorithm calculations

---

#### User Story 2 (Sarah)  [UI Developement]
**As a:** front-end developer,   
**I want:** to design and implement a user flow for selecting a job position and completing a corresponding skills and education questionnaire,   
**So that:** the system can display a weighted compatability percentage and provide clear feedback on missing skills or required qualifications.   

##### Effort
Level:

##### Acceptance Criteria
Given: the homepage loads  
When: the user opens the career dropdown  
Then: a searchable list of careers from O*NET is displayed

Given: a career is selected  
When: the user navigates to the survey page  
Then: all required skills, education, and experience are shown.

Given: The survey is completed  
When: the form is submitted  
Then: the system displays the results page with match %, matched skills, and missing skills.

---

#### User Story 3 [UX Design]
**As a:** user  
**I want:** the web interface and PDF to be clean, intuitive, and visually appealing  
**So that:** I can navigate the site easily and understand my results.

##### Effort Level: 

##### Acceptance Criteria:
Given: any page is loaded  
When: the user interacts with elements  
Then: fonts, colors, buttons, and layout are consistent and readable  
    AND the PDF design to match the website design.

---

#### User Story 4 (Lisa) [PDF Generation]
**As a:** user,  
**I want:** to receive a PDF of my career analysis  
**So that:** I can review and access these insights at a later date.  

##### Effort
Level	:   2

##### Acceptance Criteria
Given: the results page is displayed  
When : the user clicks the "Download PDF" button  
Then : a PDF is generated with:
- Career Name and Discription
- Match Percentage
- Matched Skills, Education, and Experience
- Missing Skills, Education, and Experience
    AND the PDF downloads automatically.

---

#### User Story 5 (Kassidy) [Results Page Display]
**As a:** user who has selected a career and completed the survey,  
**I want:**  to see how my selected skills compare to the required skills for that career,  
**So that:**  I can understand my skill gaps, match percentage, and the skills I have that apply to the career.  

##### Effort
Level	:   

##### Acceptance Criteria
Given: the survey is completed  
When : the results page loads  
Then : Then it displays:
- Career Name and Discription
- Match Percentage
- Matched Skills, Education, and Experience
- Missing Skills, Education, and Experience
- A "Download PDF" Button that downloads a PDF version of the results

---

#### User Story 6 [Career Selection]
**As a:** user,  
**I want:**  to select a desired career from a searchable dropdown,
**So that:**  I can begin assessing my skills, education, and experience.  

##### Effort
Level	:   

##### Acceptance Criteria
Given: the homepage loads  
When : the user opens the dropdown  
Then : the list of careers appears and is searchable with a Trie Tree algoithm.   

Given: a career is selected  
When:  the user clicks "Next"  
Then: the survey page loads with the correct career's required skills.

---

#### User Story 7 [Background Survey]
**As a:** user,  
**I want:**  to complete a survey of skills, education, and experience for the selected career  
**So that:**  the system can determine my skill gap.  

##### Effort
Level	:   

##### Acceptance Criteria
Given: the survey page is displayed  
When : the user selects Yes/No for each item  
Then : the selections are recorded

Given: the survey is submitted  
When: the backend processes the data  
Then: the results page displays:
- Career Name and Discription
- Match Percentage
- Matched Skills, Education, and Experience
- Missing Skills, Education, and Experience
- A "Download PDF" Button that downloads a PDF version of the results

---

#### User Story 8 [Trie Tree Search]
**As a:** user  
**I want:** to search for careers in a responsive, auto-complete dropdown  
**So that:** I can quickly find and select my desired career.

##### Effort Level: 

##### Acceptance Criteria:
Given: the dropdown is displayed  
When: the user types a few letters  
Then: the system suggests matching career names in real time  
    AND the search is fast and responsive for all careers in the dataset.

---

#### User Story 9 [Match Percentage Algorithm]
**As a:** user  
**I want:** the system to calculate how closely my skills, education, and experience match the selected career  
**So that:** I know what I have vs. what I still need.

##### Effort Level: 

##### Acceptance Criteria:
Given: the user completes the survey  
When: the match % algorithm runs  
Then: a numerical match percentage is calculated  
    AND missing skills, education, or experience are identified.

---

#### User Story 10 [Test-Driven Development/Automated Testing]
**As a:** developer  
**I want:** to write automated tests for backend adn frontend features using TDD principles    
**So that:** I can ensure the system works correctly, catches bugs early, and maintains reliability.

##### Effort Level: 

##### Acceptance Criteria:
Given: a new backend development  
When: a unit test runs  
Then: it verifies the endpoint returns correct data and handles errors.

Given: a new frontend component  
When: automated tests are run  
Then: it verifies correct rendering, user input handling, and interaction flow.

Given: the overall system  
When: end-to-end tests run  
Then: it verifies that user flow works as expected.  

---

#### User Story 11 [Flask and SQL]
**As a:** back-end developer  
**I want:** to set up the Flask framework and SQL database for the project  
**So that:** the application has a stable backend environment to build API endpoints and store/retrieve data.

##### Effort Level: 

##### Acceptance Criteria:
Given: a backend route needs to retrieve data  
When: a request is made  
Then: it successfully queries the database and returns the expected result.