-- =====================================
-- Query 1
-- Show all students
-- =====================================

SELECT * FROM students;

-- =====================================
-- Query 2
-- Show students from CE class
-- =====================================

SELECT *
FROM students
WHERE class = 'CE';

-- =====================================
-- Query 3
-- Show student name, subject and marks
-- =====================================

SELECT
    students.student_name,
    subjects.subject_name,
    marks.marks
FROM marks
JOIN students
ON students.student_id = marks.student_id
JOIN subjects
ON subjects.subject_id = marks.subject_id;

-- =====================================
-- Query 4
-- Average marks of every student
-- =====================================

SELECT
    student_id,
    AVG(marks) AS average_marks
FROM marks
GROUP BY student_id;

-- =====================================
-- Query 5
-- Highest marks
-- =====================================

SELECT
    MAX(marks) AS highest_marks
FROM marks;