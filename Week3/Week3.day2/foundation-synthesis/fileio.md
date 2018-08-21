## Foundation - File I/O Review

#### Also covered: while loops for input, regular expressions, string formatting

* You are going to write two programs, one that inputs informatio personnel database.

#### Group project:

* Work in groups of 2 or 3 on this project.

* Plan it out. 

* Think of the functions you will need, what their inputs (argument list) 
  should be and what their outputs (return values) should be. With a plan, 
  its easier to break up work between multiple people.

#### Input program:

* Create a loop that inputs a First Name, a Last Name, a Title, and a Salary

* * Loop input until 'done' is entered for First Name.

```
Input first name: Carter
Input last name: Adams
Input job title: Fake Instructor
Input salary: 0.00

Input first name: Kenso
Input last name: Trabing
Input job title: Real Instructor
Input salary: 18000.00

Input first name: done
```

* * Keep track of the values as a list.

* * After 'done' is entered, save the file with one record per line of the format:
```
"First Name" "Last Name" "Title" $Salary
```
Where First Name, Last Name, and Title are strings enclosed in
quotation marks and Salary is a float preceded by a $

for example, a line might look like

"Carter" "Adams" "Fake Instructor" $0.00
"Kenso" "Trabing" "Real Instructor" $18000.00
"Greg" "Smith" "GregCoin Founder" $5000000.00

#### Output program:

* Display a table based on the data in the file. It should be
formatted in an attractive way with rows of uniform width and
borders. Here is an example output:

```
+------------+------------+--------------------+------------+
| First Name | Last Name  | Job Title          | Salary     |
+------------+------------+--------------------+------------+
| Carter     | Adams      | Fake Instructor    |$0.00       |
| Kenso      | Trabing    | Real Instructor    |$18000.00   |
| Greg       | Smith      | GregCoin Founder   |$5000000.00 |
+------------+------------+--------------------+------------+
```
