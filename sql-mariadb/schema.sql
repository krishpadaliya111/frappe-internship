-- =====================================
-- Database: College
-- =====================================

CREATE DATABASE IF NOT EXISTS college;

USE college;

-- =====================================
-- Students Table
-- =====================================

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    class VARCHAR(20)
);

-- =====================================
-- Subjects Table
-- =====================================

CREATE TABLE subjects (
    subject_id INT PRIMARY KEY,
    subject_name VARCHAR(100)
);

-- =====================================
-- Marks Table
-- =====================================

CREATE TABLE marks (
    mark_id INT PRIMARY KEY,
    student_id INT,
    subject_id INT,
    marks INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);

-- =====================================
-- Insert Students
-- =====================================

INSERT INTO students VALUES
(1,'Krish','CE'),
(2,'Rahul','CE'),
(3,'Priya','IT');

-- =====================================
-- Insert Subjects
-- =====================================

INSERT INTO subjects VALUES
(101,'Python'),
(102,'SQL'),
(103,'Java');

-- =====================================
-- Insert Marks
-- =====================================

INSERT INTO marks VALUES
(1,1,101,90),
(2,1,102,88),
(3,2,101,75),
(4,2,103,82),
(5,3,102,95);