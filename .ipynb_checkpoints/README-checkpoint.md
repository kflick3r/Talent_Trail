# Talent Trail
Team 1's Group Project for 3308 Spring 2026

## Description
Talent Trail is a web-based career gap analysis tool that creates personalized reports to help users pursue their professional goals. Users select their desired career, complete a survey of their current skills, education, and experience, and Talent Trail produces a report that analysis the skill gaps needed to plan for potential careers. 

People often struggle to evaluate their skill sets and develop a comprehensive plan to achieve their desired career. Figuring out what is needed to reach a dream career can be overwhelming and time-intensive, with conflicting information across the internet. Talent Trail aligns real-world requirements from O*NET's database with a user’s current skills, education, and experience to develop a tangible and digestible analysis.  

## Team Members
- **Lisa Wilder** (GitHub: `Wilder407`, Email: Lisa.Wilder@colorado.edu)
- **Kassidy Flick** (GitHub: `kflick3r`, Email: kassidy.flick@colorado.edu)
- **Mark Olmscheid** (GitHub: `Olmscheid`, Email: Mark.Olmscheid@colorado.edu)
- **Sarah Suliman** (GitHub: `sssuliman`, Email: Sarah.Suliman@colorado.edu)

## Minimum Viable Product

1. Present available occupations to the user
2. Accept and process user-provided qualification data
3. Retrieve the occupational requirements associated with a selected job
4. Compare user data to occupational requirements / education distribution
5. Display the comparison results in a readable format

### User Flow
1. User lands on homepage
2. User selects career from searchable dropdown (Trie-based search)
3. Backend retrieves:
- Career description
- Required skills list
4. User completes survey (Yes/No or 1–5 scale)
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

## Tech Stack
- Backend: Python, Flask
- Database: PostgreSQL 
- Frontend: HTML, React
- Version Control: Github
- PDF Generation: Generate HTML and Convert to PDF (or Python reportlab)

---

## Installation / Usage
