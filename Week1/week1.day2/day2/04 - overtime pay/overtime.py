## Day 2 - Exercise 4 - Pay

# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
hours = float(input("How many hours have you worked? \n"))
rate = float(input("What is your hourly rate?\n"))
salary = ""
overtime = ""

# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
if hours <= 40:
    salary = hours* rate
    print(salary)
elif hours > 40:
    overtime = (1.5 * (hours-40) * rate)
    salary = 40 * rate
    print (salary + overtime)

# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. 

# Do not worry about error checking the user input - assume the user types numbers properly.
