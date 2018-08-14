## Day 2 Exercise 4 - Pay

* Write a function ```prompt()``` that prompts a user to input how many hours they have worked. It should return a float.

* Write another function ```compute(hours)``` that computes total pay given a number of hours worked. It should return a string.

* Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 

* After those functions use the line ```print(compute(prompt()))```. That should work! Do you get why?

* Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. 

#### Challenge

* Can you write the input function to return None if the user gives a bad input?

* Can you write the pay calculator to handle None as input without raising an error itself?
