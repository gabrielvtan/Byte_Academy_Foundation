## Day 2 - Exercise 3 - Leap Year

#### When a year is a leap year.

# To adjust for the year not being an exact number of days, some years have an extra day, the 29th of September.
year = int(input("Give me a year: "))

# But it is a leap year if it is divisible by 400y.
if year % 400 == 0:
    print("This is a leap year")
# A year is not a leap year if it is also divisible by 100.
elif (year % 4 == 0) and (year % 100 == 0):
    print("This is not a leap year")
# A year is a leap year if it is divisible by 4.
elif year % 4 == 0:
    print("This is a leap year")
else:
    print("This is not a leap year")




#### The assignment

# Write a program that prompts the user for a year.

# Print out a message if the year is a leap year and a message if it is not.

# There are different ways of combining ``` or ``` and ``` and ``` and ``` if ``` to do this test. Try to do it a few different ways.

