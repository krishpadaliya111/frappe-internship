1. Describe the difference between mutable and immutable types in Python, with examples.

Answer:

In Python, objects are classified into mutable and immutable types.

Mutable Objects

A mutable object can be changed after it is created without creating a new object.

Examples of mutable types:

List (list)
Dictionary (dict)
Set (set)

Example:

numbers = [10, 20, 30]

numbers.append(40)

print(numbers)

Output:

[10, 20, 30, 40]

The original list is modified by adding a new element.

Immutable Objects

An immutable object cannot be changed after it is created. Any modification creates a new object.

Examples of immutable types:

Integer (int)
Float (float)
String (str)
Tuple (tuple)
Boolean (bool)

Example:

name = "abc"

name = name + " def"

print(name)

Output:

abc def

A new string object is created instead of modifying the original string.



2. Write a Python program to check whether a number is a palindrome.

Answer:

number = input("Enter a number: ")

reverse = number[::-1]

if number == reverse:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

Sample Output:
Enter a number: 121

The number is a palindrome.

Explanation:

The user enters a number.
The string slicing [::-1] reverses the number.
If the original number and reversed number are the same, it is a palindrome.



3. What is a Python decorator? Provide and explain one example.

Answer:

A decorator is a special function in Python that adds extra functionality to another function or method without changing its original code.

Decorators are written using the @ symbol.

One commonly used decorator is @property, which allows a method to be accessed like an attribute.

Example:

class Student:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

student = Student("abc")
print(student.name)

Output:
abc

Explanation
@property converts the name() method into a property.
Instead of writing student.name(), we simply write student.name.
This improves readability and allows controlled access to object data.



4. Explain the purpose of __init__ in a Python class.

Answer:

The __init__() method is a special method in Python known as the constructor. It is automatically called whenever a new object of a class is created.

Its main purpose is to initialize the object's attributes with the values provided during object creation.

Example:

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
student = Student("abc", 21)
print(student.name)
print(student.age)

Output:
abc
21

Explanation
__init__() is automatically executed when Student("abc", 21) is called.
It initializes the object's attributes (name and age).
This ensures every object starts with the required data.



5. Difference between a list and a tuple — when would you use each?

Answer:

Both lists and tuples are used to store multiple items in Python, but they have some important differences.

List
A list is mutable, which means its elements can be changed after it is created.
Lists use square brackets [].
Use a list when you need to add, remove, or modify items.

Example:

fruits = ["Apple", "Banana", "Mango"]
fruits.append("Orange")
print(fruits)

Output:

['Apple', 'Banana', 'Mango', 'Orange']

Tuple
A tuple is immutable, which means its elements cannot be changed after it is created.
Tuples use parentheses ().
Use a tuple when the data should remain constant.

Example:

colors = ("Red", "Green", "Blue")
print(colors)

Output:

('Red', 'Green', 'Blue')



6. Explain var vs let vs const in JavaScript with examples.

Answer:

In JavaScript, var, let, and const are used to declare variables.

var
Old way of declaring variables.
Can be reassigned.
Function-scoped.

Example:

var name = "abc";
name = "defg";
console.log(name);

Output:

defg


let
Modern way to declare variables.
Can be reassigned.
Block-scoped.

Example:

let age = 20;
age = 21;
console.log(age);

Output:

21

const
Used for values that should not be reassigned.
Block-scoped.
Must be initialized when declared.

Example:

const country = "India";
console.log(country);

Output:

India



7. Write a for loop printing even numbers 1–10, and a while loop that doubles from 1 until ≥ 100.

Answer:
(a) for Loop

print("Even numbers from 1 to 10:")
for i in range(2, 11, 2):
    print(i)

Output:

Even numbers from 1 to 10:
2
4
6
8
10

(b) while Loop
number = 1

while number < 100:
    print(number)
    number = number * 2
print(number)

Output:

1
2
4
8
16
32
64
128

Explanation:

The loop starts from 1.
Each iteration doubles the number.
The loop stops when the number becomes 100 or greater.



8. Document each step you took to install Frappe bench, including issues and fixes.
9. Show output of `bench start` and `bench new-site` (screenshot) and explain what each did.

Answer: Question 8,9 are not assigned in task.



10. Write a SQL query joining your students, subjects, and marks tables to list each student's average mark.

Answer:

SELECT
    students.student_name,
    AVG(marks.marks) AS average_marks
FROM marks
JOIN students
ON students.student_id = marks.student_id
JOIN subjects
ON subjects.subject_id = marks.subject_id
GROUP BY students.student_name;


Sample Output:
+--------------+---------------+
| student_name | average_marks |
+--------------+---------------+
| abc         | 89.00         |
| defg        | 78.50         |
| hij         | 95.00         |
+--------------+---------------+

Explanation:

JOIN combines data from the students, subjects, and marks tables.
AVG() calculates the average marks for each student.
GROUP BY groups the records by student name so the average is calculated separately for each student.