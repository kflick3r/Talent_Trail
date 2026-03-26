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
| description | O*NET-SOC (Occupation) Description | Nullable |

### Relationships
- One-to-many with 'skills'
- One-to-many with 'education_talents_experience'

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
| onetsoc_code | Unique group identifier | Primary key |
| element_id | Group display name | NOT NULL |
| scale_id | Scale reference | Foreign key → users.id |
| FOREIGN KEY (onetsoc_code) | Connection to table | Foreign key -> occupation_data(onetsoc_code) |
| FOREIGN KEY (element_id) | Connection to table | Foreign Key -> content_model_reference(element_id) |
| FOREIGN KEY (scale_id) | Connection to table | Foreign Key -> scales_reference(scale_id))
| data_value  | Creation timestamp | NOT NULL |
| n | sample size | NOT NULL |
| standard_error | Standard error | Nullable |
| lower_ci_bound | Lower 95% CI | Nullable |
| upper_ci_bound | Upper 95% CI | Nullable |
| recommend_suppress | Low precision indicator | Char (Y=yes, N=no) |
| not_relevant | Not relevant for the occupation | Char (Y=yes, N=no) |
| date_updated | date when data was updated | NOT NULL |
| domain_source | source of data | Nullable |


### Relationships
- Many-to-one with `occupation`
- Many-to-one with `content_model_references`
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

## 5) Table: ete_categories (TESTS)

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
Stores education, training and experience data for career.

### Fields
| Field Name | Description | Constraints |
|----------|------------|-------------|
| onetsoc_code | Unique group identifier | Primary key |
| element_id | content model outline position | NOT NULL |
| scale_id | scale id | NOT NULL |
| category | percent frequency category | NOT NULL |
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
| FOREIGN KEY (element_id, scale_id, category) |  | Foreign Key -> ete_categories(element_id, scale_id, category)|


### Relationships
- Many-to-one with content_model_reference
- Many-to-one with ete_categories
- Many-to-one with occupation_data
- Many-to-one with scales_reference
- Composite primary key (`element_id`, `scale_id, category`)

### Table Tests

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


### Table Tests

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

## Access Method: get_groups_for_user

### Description
Returns all groups a user belongs to.

### Parameters
- user_id (int)

### Return Values
- List of group objects

### Tests
1. User with memberships returns groups
2. User with none returns empty list

---

## Access Method: get_tasks_for_group

### Description
Returns tasks associated with a group.

### Parameters
- group_id (int)

### Return Values
- List of tasks

### Tests
1. Tasks returned for valid group
2. Empty list for group with no tasks

---

## Access Method: get_availability_overlap

### Description
Computes overlapping availability for a group.

### Parameters
- group_id (int)

### Return Values
- List of overlapping time windows

### Tests
1. Overlapping windows returned for common availability
2. Empty list when no overlap exists

---

# Page-to-Database Mapping

| Page | Tables Accessed |
|----|----------------|
| Landing Page | N/A |
| Career Selection Page | occupation_data, skills, education_training_experience |
| Survey Page | content_model_reference, user_responses |
| Results Page | user_responses, occupation_data |

---

# Page Data Access Tests

**Use Case Name:** Dashboard loads user data  
**Description:** Verify dashboard queries correct tables  
**Pre-conditions:** User logged in  
**Test Steps:**
1. Load dashboard
2. Fetch groups and tasks  
**Expected Result:** Correct data displayed  
**Post-conditions:** None  

---

## Notes
- Constraints enforced at DB and ORM levels
- All access methods wrapped in service layer
- Tests executable via integration test suite
