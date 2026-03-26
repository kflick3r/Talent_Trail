# SQL_TESTING.md
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

The backend uses **SQL** accessed through **SQLite3** via a Flask.

---

# Database Tables

At minimum, the system requires the following tables:
- `occupation_data`
- `skills`
- `user_responses`
- `content_model_reference`
- `education_training_experience`
- `ete_categories`
- `scales_reference`

Each table is described below.

---

## 1) Table: occupation_data

### Table Description
Represents the available occupation/career options. Stores core occupation information from O*NET.

### Fields
| Field Name | Description | Constraints |
|----------|------------|-------------|
| onetsoc_code | Unique O*NET-SOC Code | PRIMARY KEY, NOT NULL |
| title | O*NET-SOC (Occupation) Title | NOT NULL |
| description | O*NET-SOC (Occupation) Description | NOT NULL |

### Relationships
- One-to-many with `skills`
- One-to-many with `education_training_experience`

### Table Tests

**Use Case Name:** Double Code INSERT (Prevent duplicate occupation)
**Description:** Attempt to insert a duplicate onetsoc_code into the database
**Pre-conditions:** Database running  

**Test Steps:**
1. Insert valid onetsoc_code
2. Insert valid onetsoc_code into database with different description

**Expected Result:** Second insert test fails
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
| onetsoc_code | Unique group identifier | NOT NULL, FK → occupation_data |
| element_id | Group display name | NOT NULL, FK → content_model_reference  |
| scale_id | Scale reference | NOT NULL, FK → scales_reference |
| data_value  | Creation timestamp | NOT NULL |
| n | sample size | NULLABLE |
| standard_error | Standard error | NULLABLE |
| lower_ci_bound | Lower 95% CI | NULLABLE |
| upper_ci_bound | Upper 95% CI | NULLABLE |
| recommend_suppress | Low precision indicator (Y/N) | NULLABLE |
| not_relevant | Relevance flag (Y/N) | NULLABLE |
| date_updated | date when data was updated | NOT NULL |
| domain_source | source of data | NOT NULL |


### Relationships
- Many-to-one with `occupation_data`
- Many-to-one with `content_model_references`
- Many-to-one with `scales_reference`

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
Stores user-selected values for career and skill survey responses and a unique response_id to connect through the tables.

### Fields
| Field Name | Description | Constraints |
|----------|------------|-------------|
| response_id | Unique response identifier | Primary Key, Autoincrement |
| onetsoc_code | Associated selected occupation | NOT NULL, FK → occupation_data |
| element_id | Content Model Element | NOT NULL, FK → content_model_reference |
| scale_id | Scale reference | NULLABLE, FK → scale_reference |
| user_value | Value selected by user | NULLABLE |
| created_at | Timestamp of respone | NULLABLE |

### Relationships
- Many-to-one with `occupation_data`
- Many-to-one with `content_model_reference`
- Many-to-one with `scales_reference`

### Table Tests

**Use Case Name:** Insert valid user response  
**Description:** Verify a response can be stored  

**Test Steps:**
1. Insert response with valid foreign key  

**Expected Result:** Insert succeeds  
**Actual Result:**  
**Status:** Pass  

---

## 4) Table: content_model_reference (NEEDS Test Review)

### Table Description
Defines content model elements such as skills and abilities. Tracks elements such as cognitive abilities, worker characteristics, oral comprehension, etc. 

### Fields
| Field Name | Description | Constraints |
|----------|------------|-------------|
| element_id | Task identifier | PRIMARY KEY |
| element_name | Content Model Element Name| NOT NULL |
| description | Content Model Element Description | NULLABLE |

### Relationships
- One-to-many with `education_training_experience`
- One-to-many with `skills`
- One-to-many with `ete_categories`


### Table Tests

**Use Case Name:** element_id 
**Description:** Verify element_id persistence  

**Test Steps:**
1. Insert element_id 
2. Query by element_id  

**Expected Result:** Element 
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
| FOREIGN KEY (element_id) |  | Foreign Key -> content_model_reference(element_id)|
| FOREIGN KEY (scale_id) |  | Foreign Key -> scales_reference(scale_id) |
| category | Category value associated with element | Foreign key |
| category_description | category description of element | NOT NULL |
| Primary Key (element_id, scale_id, category) | one combination of three variables | unique |

### Relationships
- Many-to-one with content_model_reference
- Many-to-one with scales_reference
- One-to-many with education_training_experience

### Table Tests

**Use Case Name:** Composite key uniqueness   

**Test Steps:**
1. Insert valid category row  
2. Insert duplicate (same element_id, scale_id, category)  

**Expected Result:** Second insert fails  

---

## 6) Table: education_training_experience

### Table Description
Stores education, training and experience data for career.

### Fields
| Field Name | Description | Constraints |
|----------|------------|-------------|
| onetsoc_code | Occupation reference | NOT NULL, FK → occupation_data (onetsoc_code) |
| element_id | content model element | NOT NULL, FK → content_model_reference (element_id) |
| scale_id | scale reference id | NOT NULL, FK → scales_reference (scale_id) |
| category | ETE category | NULLABLE, FK → ete_category (category) |
| data_value  | Rating associated with the O*NET-SOC occupation | NOT NULL |
| n | sample size | NOT NULL |
| standard_error | Standard error | NULLABLE |
| lower_ci_bound | Lower 95% CI | NULLABLE |
| upper_ci_bound | Upper 95% CI | NULLABLE |
| recommend_suppress | Low precision indicator | Char (Y=yes, N=no) |
| not_relevant | Not relevant for the occupation | Char (Y=yes, N=no) |
| date_updated | date when data was updated | NOT NULL |
| domain_source | source of data | NULLABLE |


### Relationships
- Many-to-one with `content_model_reference`
- Many-to-one with `ete_categories` via composite foreign key (`element_id`, `scale_id, category`)
- Many-to-one with `occupation_data`
- Many-to-one with `scales_reference`

### Table Tests

**Use Case Name:** Verify ETE row insertion  

**Test Steps:**
1. Insert valid row with existing `element_id`, `scale_id`, `category`, and `onetsoc_code`  
2. Query the row by occupation and element  

**Expected Result:** Row is stored and returned successfully  

**Post-conditions:** Database remains consistent

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


### Table Tests

**Use Case Name:** Insert Scale  

**Test Steps:**
1. Insert Valid scale

**Expected Result:** Insert succeeds  

---

# Data Access Methods

Each table has at least one access method.

---

## Access Method: get_careers

### Description
Retrieves all occupations that have at least one associated skill.

### Parameters
- none

### Return Values
- List of tuples: `(onetsoc_code, title)`

### Tables Accessed
- `occupation_data`
- `skills`

### Tests

**Use Case Name:** Retrieve career list

**Test Steps:**
1. Call `get_careers()`

**Expected Result:** Returns list of careers sorted alphabetically  
**Post-conditions:** None  

---

## Access Method: get_skills

### Description
Retrieves the top 10 most important skills for a selected occupation.

### Parameters
- `onetsoc_code` (string)  

### Return Values
- List of tuples: `(element_name, data_value, description)`

### Tables Accessed
- `skills`
- `content_model_reference`

### Tests

**Use Case Name:** Valid occupation skills  

**Test Steps:**
1. Call with valid `onetsoc_code()`

**Expected Result:** Returns up to 10 skills sorted by importance  
**Post-conditions:** None  

---

## Access Method: get_career_name

### Description
Retrieves the title of a career from its O*NET code.

### Parameters
- `onetsoc_code` (string)  

### Return Values
- String (career title) or `"Unknown Career"`

### Tables Accessed
- `occupation_data`

### Tests

**Use Case Name:** Valid career lookup  

**Test Steps:**
1. Call with valid `onetsoc_code()`

**Expected Result:** Returns correct career title  
**Post-conditions:** None  

---

## Access Method: get_skill_levels_and_importance

### Description
Retrieves O*NET Level (LV) and Importance (IM) values for selected career. 

### Parameters
- `onetsoc_code` (string)
- `skill_names` (list of strings)

### Return Values
- List of dictionaries containing:
  - `skill_name`
  - `onet_level`
  - `onet_importance` 

### Tables Accessed
- `skills`
- `content_model_reference`

### Tests

**Use Case Name:** Valid skill comparison data  

**Test Steps:**
1. Provide valid occupation and skill list

**Expected Result:** Returns level and importance value  
**Post-conditions:** None  

---

# Page-to-Database Mapping

| Page | Tables Accessed |
|----|----------------|
| Landing Page | None |
| About Page | None |
| Career Selection Page | occupation_data, skills |
| Career Survey Page | skills, content_model_reference, occupation_data, user_responses |
| Results Page | user_responses, skills, education_training_experience, occupation_data |

---

# Page Data Access Tests

**Use Case Name:** Load career selection page

**Test Steps:**
- Navigate to /careers
- Load dropdown

**Expected Result:** 
List of careers is displayed

---

**Use Case Name:** Load survey page

**Test Steps:**
- Select career
- Submit selection

**Expected Result:**
Top 10 skills displayed

---

**Use Case Name:** Invalid career selection

**Test Steps:**
- Submit empty or invalid career

**Expected Result:**
Error message displayed

---

## Notes
- O*NET database and user_responses uses SQLite3 and is accessed directly through Python’s sqlite3 module  
- SQL queries are written inside Flask route helper functions
- Data is based on the O*NET dataset and it is following it's structure
- Testing is performed manually through the application workflows and by direct SQL queries

