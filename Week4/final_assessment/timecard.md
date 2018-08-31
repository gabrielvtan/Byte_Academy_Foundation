## Foundation Assessment

#### Timecard system

* A company uses a terminal program to keep track of employee hours worked.

* Users have an id number, the boss's id number is 0

* Don't worry about passwords / PIN

* The program should ask for a user's id. It can be a new id or an existing one

* If it is an employee id (an integer) ask how many minutes they worked today. Store the result and exit the program.

* You should save the entered amounts into a single file that adds data each time the program is run.

* If it is the boss's id, it should print how many total minutes correspond to each user id.

* So if user 100 has used the program 3 times and has entered 60, 120, and 180, and user 200 has used the program 1 time and has enterd 90, the boss will see something like:

```
Enter your EmployeeID: 0

EMPLOY  ID          MINUTES WORKED
100                 360
200                 90
```

* Get the employee part of the program working first. Have a file that grows with a meaningful record each time an employee enters new data. Then work on calculating the sums. Remember that you don't have to score a 100 to pass an exam. You've got this.

* It's been a real pleasure teaching you all!

#### Bonus

* Allow employees to enter time in HH:MM format with hours and minutes, such as 6:30 for 390 minutes

* Implement PIN numbers and a user creation step.