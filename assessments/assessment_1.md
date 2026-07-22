ASSESSMENT-1

1. Describe the difference between mutable and immutable types in Python, with examples.

Answer:

In Python, every value is stored as an object. These objects are mainly divided into mutable and immutable types based on whether their contents can be changed after they are created.

Mutable Types
A mutable object is one whose data can be modified after it is created. When we change a mutable object, Python updates the existing object instead of creating a new one.

Common mutable data types are:
•	List (list) 
•	Dictionary (dict) 
•	Set (set) 
•	Bytearray (bytearray) 

Example

numbers = [10, 20, 30]

numbers.append(40)

print(numbers)	

Output
[10, 20, 30, 40]

Here, the original list is modified by adding a new element. Python does not create another list; it updates the existing one.

Real-life Use of Mutable Types
Suppose you are building an attendance management system.
Initially, today's attendance list is empty.

attendance = []

As students arrive, you keep adding their names.

attendance.append("Krish")

attendance.append("Rahul")

attendance.append("Priya")

Since the attendance keeps changing throughout the day, using a list (mutable) is the correct choice.

Immutable Types
An immutable object cannot be modified after it is created. If we try to change its value, Python creates a completely new object instead of modifying the existing one.

Common immutable data types are:
•	Integer (int) 
•	Float (float) 
•	String (str) 
•	Tuple (tuple) 
•	Boolean (bool) 

Example

name = "Krish"

name = name + " Padaliya"

print(name)

Output
Krish Padaliya
Although it appears that the string was modified, Python actually creates a new string object because strings are immutable.

Real-life Use of Immutable Types
Consider an Aadhaar Number, PAN Number, or Student Roll Number.
Once these values are assigned, they should never change accidentally.

Example:

roll_number = "CE23045"

Keeping such values immutable makes the program safer because no part of the code can accidentally modify them.


2. Write a Python program to check whether a number is a palindrome.

Answer

A palindrome is a number or word that remains the same when read from left to right or right to left.

Examples:
121
1331
4554
These are palindrome numbers because reversing them gives the same number.

Python Program

number = input("Enter a number: ")

reverse = number[::-1]

if number == reverse:

    print("The number is a palindrome.")

else:

    print("The number is not a palindrome.")

Sample Output

Enter a number: 121

The number is a palindrome.

Real-life Use
Palindrome checking is not only used in interview questions. Similar logic is useful in:
•	Data validation 
•	Pattern recognition 
•	String processing 
•	Basic cryptography practice 
•	Competitive programming 
It also helps beginners understand string manipulation, comparison, and conditional statements.


3. What is a Python decorator? Provide and explain one example.

Answer

A decorator is a special feature in Python that allows us to add extra functionality to a function or method without changing its original code.
Instead of modifying the original function, a decorator wraps it and performs additional work before or after the function executes.
Decorators are written using the @ symbol.

Why are decorators useful?
Suppose many functions need to perform the same task before running, such as:
•	Checking user login 
•	Measuring execution time 
•	Printing logs 
•	Validating input 
Instead of writing the same code inside every function, we can write one decorator and reuse it.

Example using @property

class Student:

    def __init__(self, name):

        self._name = name

    @property

    def name(self):

        return self._name

student = Student("Krish")

print(student.name)


Output
Krish

Explanation
Normally, we call methods using parentheses.

Example

student.name()

But because of the @property decorator, we can access it like an attribute.

student.name

This makes the code more readable while still allowing the class to control how the value is accessed.

Real-life Use
Suppose you are building an Employee Management System.
Each employee has a salary.
You want users to read the salary like this:
employee.salary
instead of
employee.get_salary()
Using @property makes the code cleaner while still allowing you to perform validation or calculations in the background.

4. Explain the purpose of __init__ in a Python class.

Answer

The __init__() method is a special method in Python called the constructor.
It is automatically executed whenever a new object of a class is created.
Its main purpose is to initialize the object's attributes with the values provided during object creation.
	
Example

class Student:

    def __init__(self, name, age):

        self.name = name
 
        self.age = age

student = Student("Krish", 21)

print(student.name)

print(student.age)

Output
Krish
21

Real-life Use
Imagine an online shopping application.
Every product has:
•	Product ID 
•	Product Name 
•	Price 
Instead of assigning these values one by one after creating the object, we initialize them immediately.

5. Difference between a List and a Tuple — When Would You Use Each?

Answer

In Python, both lists and tuples are data structures used to store multiple values in a single variable. They can store different types of data such as integers, strings, or even other lists. The main difference between them is whether their contents can be changed after creation.
List
A list is a mutable data type, which means its elements can be added, removed, or modified after the list is created.
Lists are created using square brackets [].


Example

fruits = ["Apple", "Banana", "Mango"]

fruits.append("Orange")

fruits[0] = "Grapes"

print(fruits)

Output

['Grapes', 'Banana', 'Mango', 'Orange']

In this example, a new fruit is added and the first fruit is changed. This is possible because lists are mutable.
When to Use a List
Lists are useful when the data changes frequently.
For example:
•	Shopping cart items in an e-commerce application. 
•	Student attendance records. 
•	Tasks in a to-do list. 
•	Chat messages in a messaging application. 
If users need to add or remove information, a list is usually the best choice

Tuple
A tuple is an immutable data type, which means its elements cannot be modified after it is created.
Tuples are created using parentheses ().

Example

student = ("Krish", 21, "Computer Engineering")

print(student)

Once the tuple is created, its values cannot be changed.

If we try:

student[0] = "Rahul"

Python will generate an error because tuples are immutable.

When to Use a Tuple
Tuples are useful when the data should remain fixed throughout the program.
Examples include:
•	Student Roll Number 
•	Date of Birth 
•	GPS Coordinates 
•	RGB Color Values 
•	Database records that should not be modified accidentally 
Using tuples prevents accidental modification of important information.

Real-Life Example
Imagine you are developing a college management system.
The list of students attending today's lecture changes as students arrive.
attendance = ["Krish", "Rahul"]
attendance.append("Priya")
A list is appropriate because attendance changes.
Now consider a student's roll number:
roll_number = ("CE23045")
A roll number should never change after it is assigned, so immutable data is more appropriate.


6. Explain var vs let vs const in JavaScript with examples.

Answer

In JavaScript, var, let, and const are keywords used to declare variables. Although all three store data, they differ in scope, reassignment rules, and modern usage.

var
var is the traditional way of declaring variables in JavaScript.
Characteristics:
•	Function-scoped 
•	Can be reassigned 
•	Can be redeclared 

Example

var name = "Krish";

name = "Rahul";

console.log(name);

Output
Rahul

let
let was introduced in ES6 (ECMAScript 2015).
Characteristics:
•	Block-scoped 
•	Can be reassigned 
•	Cannot be redeclared in the same scope 

Example

let marks = 85;

marks = 92;

console.log(marks);

Output
92

const
const is also block-scoped but cannot be reassigned after declaration.
Characteristics:
•	Block-scoped 
•	Cannot be reassigned 
•	Must be initialized during declaration

Example

const college = "ABC Engineering College";

console.log(college);

Output
ABC Engineering College

Attempting to change it:
college = "XYZ College";
will produce an error.

Real-Life Use
Suppose you are creating an online shopping website.
The customer's name may change during editing.
let customerName = "Krish";
The GST percentage usually remains constant.
const GST = 18;


7. Write a for loop printing even numbers 1–10, and a while loop that doubles from 1 until ≥ 100.

Answer

(a) for Loop

print("Even numbers from 1 to 10:")

for number in range(2, 11, 2):

    print(number)

Output

Even numbers from 1 to 10:
2
4
6
8
10

Explanation
The range(2, 11, 2) function means:
•	Start from 2 
•	Continue until 10 
•	Increase by 2 each time 
Therefore, only even numbers are printed.

Real-Life Use
A for loop is useful when we know in advance how many times we need to repeat a task.



Examples include:
•	Displaying all students in a classroom. 
•	Printing marks of every subject. 
•	Showing products in an online shopping website. 
•	Processing every row in a database table.

(b) while Loop

number = 1

while number < 100:

    print(number)

    number = number * 2

print(number)

Output
1
2
4
8
16
32
64
128

Explanation
The loop starts with the value 1.
Each iteration doubles the value.
The loop continues until the value becomes 100 or greater.

Real-Life Use
A while loop is useful when the number of repetitions is not known in advance.
Examples include:
•	Reading data until the user chooses to exit. 
•	ATM PIN verification. 
•	Login systems. 
•	Menu-driven applications. 
•	Waiting for a network response.

8. Document each step you took to install Frappe bench, including issues and fixes.

9. Show output of `bench start` and `bench new-site` (screenshot) and explain what each did.

Answer Question 8,9 are not assigned in task.

10. Write a SQL query joining your students, subjects, and marks tables to list each student's average mark.

Answer

SELECT

    students.student_name,

    AVG(marks.marks) AS average_marks

FROM students

JOIN marks

    ON students.student_id = marks.student_id

JOIN subjects

    ON marks.subject_id = subjects.subject_id

GROUP BY students.student_name;

Explanation
SELECT
SELECT students.student_name,
       AVG(marks.marks)
This selects:
•	Student name 
•	Average marks 
JOIN
The JOIN keyword combines related data from different tables.
In this query:
•	The students table provides student names. 
•	The marks table provides marks. 
•	The subjects table connects subjects with marks. 
Although the average calculation only needs names and marks, joining the subjects table demonstrates how all three related tables work together.

AVG()
AVG() is an aggregate function.
It calculates the average of all marks belonging to each student.

Example:
Marks:
90
88
Average:
89

GROUP BY
GROUP BY students.student_name;

This groups all records belonging to the same student before calculating the average.
Without GROUP BY, SQL would try to calculate one average for the entire table instead of one average per student.

Sample Output
Student Name	   Average Marks
Krish  	           89.00
Rahul	           78.50
Priya	           95.00

Real-Life Use
Queries like this are commonly used in:
•	School and college management systems 
•	University result portals 
•	ERP software 
•	HR performance reports 
•	Sales and business analytics 

For example, instead of calculating each student's average marks manually, the database performs the calculation instantly using JOIN, AVG(), and GROUP BY
