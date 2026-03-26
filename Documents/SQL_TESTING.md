# SQL_TESTING_DRAFT.md
## Project Milestone 5: SQL Design
**Project:** Team 1: Algorithm Alliance - Talent Trail  
**Purpose:** Database design and testing specification for developers

---

## Overview

This document describes the **database schema**, **table relationships**, and **data access methods** for the Talent Trail application. It is intended as a **developer-facing design document** that clearly defines how data is stored, accessed, and validated.

This document answers the following questions:
- What tables exist in the database?
- What fields and constraints do those tables contain?
- How are tables related?
- What data access methods are required?
- Which pages depend on which data?
- How do we test both the schema and the access routines?

The backend uses **SQL** accessed through **SQLite3** via Flask.

---

# Database Tables

At minimum, the system requires the following tables:
- `occupation_data`
- `skills`
- `user_responses`
- `content_model`
- `education_training_experience`
- `ete_categories`
- `scales_reference`

Each table is described below.

---

## 1) Table: occupation_data

### Table Description
Represents the available occupation/career options.

### Fields
| Field Name | Description | Constraints |
|----------|------------|-------------|
| onetsoc_code | O*NET-SOC Code | PRIMARY KEY, NOT NULL |
| title | O*NET-SOC Title | NOT NULL |
| Description | O*NET-SOC Description | Nullable |

### Relationships
- One-to-many with 'skills'
- One-to-many with 'education_talents_experience'

### Table Tests

**Use Case Name:** Veriy unique onet code
**Description:** Attempt to insert a duplicate onetsoc_code into the database
**Pre-conditions:** Database running  
**Test Steps:**
1. Insert valid onetsoc_code
2. Insert valid onetsoc_code into database with different description
**Expected Result:** Test fails
**Actual Result:** 
**Status:** 
**Post-conditions:** 

---

## 2) Table: skills

### Table Description
Represents the skills that are necessary for each oppucation in occupation_data.

### Fields
| Field Name | Description | Constraints |
|----------|------------|-------------|
| onetsoc_code | Unique group identifier | Primary key |
| element_id | Group display name | NOT NULL |
| scale_id | scale id | Foreign key → users.id |
| data_value  | Creation timestamp | NOT NULL |
| n | sample size | NOT NULL |
| standard_error | Standard error | Nullable |
| lower_ci_bound | Lower 95% CI | Nullable |
| upper_ci_bound | Upper 95% CI | Nullable |
| recommend_suppress | Low precision indicator | Char (Y=yes, N=no) |
| not_relevant | Not relevant for the occupation | Char (Y=yes, N=no) |
| date_updated | date when data was updated | NOT NULL |
| domain_source | source of data | Nullable |
| FOREIGN KEY (onetsoc_code) | Connection to table | Foreign key -> occupation_data(onetsoc_code) |
| FOREIGN KEY (element_id) | Connection to table | Foreign Key -> content_model_reference(element_id) |
| FOREIGN KEY (scale_id) | Connection to table | Foreign Key -> scales_reference(scale_id)) |


### Relationships
- Many-to-one with `occupation`
- Many-to-many with `content_model_references`
- Many-to-one with `skills`

### Table Tests

**Use Case Name:**  Element_id retrieval
**Description:** Verify that the element_id is NOT NULL
**Pre-conditions:** Database running 
**Test Steps:**
1. Insert into skills with NULL attributes
**Expected Result:** Test should fail
**Actual Result:**   
**Status:** 

---

## 3) Table: user_responses 

### Table Description
Stores user career and skill survey responses and a response_id to connect through the tables.

### Fields
| Field Name | Description | Constraints |
|----------|------------|-------------|
| response_id | unique response id | Primary Key |
| onetsoc_code | chosen career | Foreign key → occupations |
| skills | top 10 user skills w | Default 'member' |

### Relationships
- Links user response to chosen skills and ete, used across the tables

### Table Tests

**Use Case Name:** Add response to table
**Description:** Verify response_id persistence
**Test Steps:**
1. Insert (response_id, onetsoc_code)
2. Query by response_id
**Expected Result:** Response exists  
**Status:** Pass  

---

## 4) Table: content_model_reference

### Table Description
Tracks elements such as cognitive abilities, worker characteristics, oral comprehension, etc. 

### Fields
| Field Name | Description | Constraints |
|----------|------------|-------------|
| element_id | Task identifier | PRIMARY KEY |
| element_name | Content Model Element Name| NOT NULL |
| description | Content Model Element Description | NOT NULL |

### Relationships
- Many-to-one with `education_training_experience`
- Many-to-one with `skills`
- Many-to-one with `ete_categories`


### Table Tests

**Use Case Name:** element_id 
**Description:** Verify element_id persistence  
**Test Steps:**
1. Insert element_id 
2. Query by element_id  
**Expected Result:** Element persists
**Status:** Pass  

---

## 5) Table: ete_categories

### Table Description
Provide descriptions of the Education, Training, and Experience percent frequency categories.

### Fields
| Field Name | Description | Constraints |
|----------|------------|-------------|
| element_id | Content Model Outline Position | NOT NULL |
| scale_id | Id from Scale table| NOT NULL |
| category | Category value associated with element | Foreign key |
| category_description | category description of element | NOT NULL |
| FOREIGN KEY (element_id) | connection to table | Foreign Key -> content_model_reference(element_id)|
| FOREIGN KEY (scale_id) | connection to table | Foreign Key -> scales_reference(scale_id) |
| Primary Key (element_id, scale_id, category) | one combination of three variables | unique |

### Relationships
- Many-to-one with content_model_reference
- Many-to-one with scales_reference
- One-to-many with education_training_experience

### Table Tests (UPDATE)

**Use Case Name:** Store availability  
**Description:** Verify availability persistence  
**Test Steps:**
1. Insert availability row  
2. Query by user_id  
**Expected Result:** Row returned  
**Status:** Pass  

---

## 6) Table: education_training_experience

### Table Description
Suggested education, training and experience requires for career.

### Fields
| Field Name | Description | Constraints |
|----------|------------|-------------|
| onetsoc_code | Unique group identifier | Primary key |
| element_id | content model outline position | NOT NULL |
| scale_id | scale id | NOT NULL |
| category | percent frequency category ] NOT NULL |
| data_value  | Rating associated with the O*NET-SOC occupation | NOT NULL |
| n | sample size | NOT NULL |
| standard_error | Standard error | Nullable |
| lower_ci_bound | Lower 95% CI | Nullable |
| upper_ci_bound | Upper 95% CI | Nullable |
| recommend_suppress | Low precision indicator | Char (Y=yes, N=no) |
| not_relevant | Not relevant for the occupation | Char (Y=yes, N=no) |
| date_updated | date when data was updated | NOT NULL |
| domain_source | source of data | Nullable |
| FOREIGN KEY (onetsoc_code) | Connection to table | Foreign key -> occupation_data(onetsoc_code) |
| FOREIGN KEY (element_id) | Connection to table | Foreign Key -> content_model_reference(element_id) |
| FOREIGN KEY (scale_id) | Connection to table | Foreign Key -> scales_reference(scale_id)) |
| FOREIGN KEY (element_id, scale_id, category) | unique connection to table | Foreign Key -> ete_categories(element_id, scale_id, category)|


### Relationships
- Many-to-one with content_model_reference
- Many-to-one with ete_categories
- Many-to-one with occupation_data
- Many-to-one with scales_reference
- Composite primary key (`element_id`, `scale_id, category`)

### Table Tests (UPDATE)

**Use Case Name:** Store availability  
**Description:** Verify availability persistence  
**Test Steps:**
1. Insert availability row  
2. Query by user_id  
**Expected Result:** Row returned  
**Status:** Pass

---

## 7) Table: scales_reference

### Table Description
Suggested education, training and experience requires for career.

### Fields
| Field Name | Description | Constraints |
|----------|------------|-------------|
| scale_id  |  | PRIMARY KEY, NOT NULL |
| scale_name |  | CHARACTER VARYING(50) NOT NULL |
| minimum |  | DECIMAL(1,0) NOT NULL |
| maximum |  | DECIMAL(3,0) NOT NULL |

### Relationships
- One-to-many with skills
- One-to-many with ete_categories
- One-to-many with education_training_experience


### Table Tests (UPDATE)

**Use Case Name:** Store availability  
**Description:** Verify availability persistence  
**Test Steps:**
1. Insert availability row  
2. Query by user_id  
**Expected Result:** Row returned  
**Status:** Pass

---

# Data Access Methods

Each table has at least one access method.

---

## Access Method: get_careers

### Description
Retrieves a list of careers that have at least one associated skill.

### Parameters
- string

### Return Values
- List of Tuples (onetsoc_code, title)

### Tests (UPDATE)

**Use Case Name:** Verify valid login  
**Pre-conditions:** User exists  
**Test Steps:**
1. Call method with known email  
**Expected Result:** User object returned  
**Post-conditions:** None  

---

## Access Method: get_skills

### Description
- Retrieves the top 10 highest-valued skills for a selected career.

### Parameters
- onetsoc_code (char)
- response_id (char)

### Return Values
- List of tuples: (skill_name, data_value, description)

### Tests (UPDATE)
1. User with memberships returns groups
2. User with none returns empty list

---

## Access Method: get_career_name

### Description
- Retrieves the readable career title from the database.

### Parameters
- onetsoc_code (char) 

### Return Values
- string: Career name or error message

### Tests (UPDATE)
1. Overlapping windows returned for common availability
2. Empty list when no overlap exists

---

# Page-to-Database Mapping

| Page | Tables Accessed |
|----|----------------|
| Landing Page | user_response |
| Career Selection | occupations |
| Career Survey | occupations, skills, education_talents_experience, user_responses |
| Results Page | user_responses |
| About Page | None |

---

# Page Data Access Tests

**Use Case Name:** Results Page loads user response data  
**Description:** Verify dashboard queries correct tables  
**Pre-conditions:** Survey completed 
**Test Steps:**
1. Load results page
2. Fetch skills and comparison score  
**Expected Result:** Correct data displayed  
**Post-conditions:** None  

---

## Notes
- User responses stored in a unique table to limit need for sessions and logins (MVP)
- Tests executable via integration test suite (in development as of 3/23/26)
