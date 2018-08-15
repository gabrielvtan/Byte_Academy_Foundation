## Foundation - Week 2 Day 2 Exercise 3 - Student Record

* Create a class representing a record of a student

* The attributes should be:
* `first_name`
* `last_name`
* `age`
* `grades` - this should be a list 

* It should have two methods:

* ```addgrade(grade)``` : appends a grade to the grades list 
* ```gpa()``` returns the student's gpa (the mean value of the grades list)

#### Challenge:

* Write ```load(filename)``` that takes the name of a file and loads data from
it. It is up to you to decide the format of how this data is stored. json might
be useful. After load() is called, the member values should all be set to values
specified in the file, possibly overwriting existing values.

* Write ```save(filename)``` that saves the data to the format you designed.
