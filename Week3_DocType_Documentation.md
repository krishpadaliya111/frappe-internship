# Week 3 – Frappe Internship

## Student Management System

This document explains the purpose and field types used in the Student Management and Product Catalogue DocTypes developed during Week 3 of the Frappe Internship.

---

# 1. Student DocType

### Purpose
Stores complete information about a student including personal details, academic details, and marks obtained in different subjects.

| Field Name | Field Type | Purpose |
|------------|-----------|---------|
| Student ID | Data | Unique identification number assigned to each student. |
| Student Name | Data | Stores the full name of the student. |
| Department | Link | Links the student to a Department DocType. |
| Date of Birth | Date | Stores the student's birth date. |
| Gender | Select | Allows selection of Male, Female, or Other. |
| Grade | Select | Stores the student's overall grade. |
| Enrollment Date | Date | Date when the student enrolled. |
| Status | Select | Indicates whether the student is Active, Inactive, Graduated, etc. |
| Notes | Small Text | Additional remarks or comments about the student. |
| Percentage | Float | Stores the student's overall percentage. (Currently entered manually; planned to be calculated automatically.) |
| Subjects | Table | Child Table that stores multiple subjects and marks for one student. |

---

# 2. Student Subject (Child Table)

### Purpose
Stores the subjects and marks of an individual student.

| Field Name | Field Type | Purpose |
|------------|-----------|---------|
| Subject Name | Data | Name of the subject. |
| Marks | Float | Marks obtained in the subject. |

Each Student can have multiple Subject records using this child table.

---

# 3. Department DocType

### Purpose
Stores the list of departments available in the institution.

| Field Name | Field Type | Purpose |
|------------|-----------|---------|
| Department Name | Data | Name of the department. |

This DocType is linked to Student using a Link field.

---

# 4. Product Catalogue DocType

### Purpose
Stores product information for a catalogue management system.

| Field Name | Field Type | Purpose |
|------------|-----------|---------|
| Product ID | Data | Unique identifier for the product. |
| Product Name | Data | Name of the product. |
| Category | Select | Product category. |
| Price | Currency | Product selling price. |
| Stock Availability | Int | Quantity available in stock. |
| Tags | Data | Keywords used for searching and filtering products. |
| Description | Small Text | Detailed information about the product. |
| Images | Table | Child Table containing product images. |

---

# 5. Product Images (Child Table)

### Purpose
Stores multiple images for a single product.

| Field Name | Field Type | Purpose |
|------------|-----------|---------|
| Image Name | Data | Name or title of the image. |
| Image URL | Attach Image | Stores the image associated with the product. |

Each Product can contain multiple images through this child table.

---

# Relationships

Student
│
├── Department (Link)
│
└── Student Subject (Child Table)
      ├── Subject Name
      └── Marks


Product Catalogue
│
└── Product Images (Child Table)
      ├── Image Name
      └── Image URL

---

# Design Choices

### Student Module

- Uses a Link field to connect with Department.
- Uses a Child Table to store multiple subjects.
- Percentage field is included for future automatic calculation.
- Designed for academic record management.

### Product Catalogue Module

- Uses a Child Table to store multiple product images.
- Uses Currency field for product pricing.
- Uses Integer field for stock quantity.
- Designed for inventory and product management.

---

# Learning Outcomes

During this task, I learned:

- Creating standard DocTypes
- Creating Child Tables
- Using Link fields
- Working with Select, Date, Currency, Float, Int, Data, Small Text, Table and Attach Image field types
- Exporting DocTypes as Fixtures
- Understanding the .json, .py and .js structure of a DocType
- Configuring Role Permissions
- Using Git and GitHub for version control