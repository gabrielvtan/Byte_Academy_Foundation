## Day 2 - Exercise 2 - Grades
#### Challenges

# Only use two print statements in your program

# Make it say "an A" instead of "a A" when the grade is an "A"

# Prompt the user to input a number between 0.0 and 1.0 (inclusive)
grade = float(input("Enter an number between 0.0 and 1.0: "))
score = ""

# If the number is less than 0.0 or greater than 1.0, give an error.
if grade < 0.0 or grade > 1.0:
    print("ERRROR: GIVE ME A CORRECT VALUE")
# If the number is greater than or equal to 0.9 the grade is an "A"
    if grade >= 0.9:
        score = "an A"
    # If the number is greater than or equal to 0.8 and less than 0.9 the grade is a "B"
    elif grade >= 0.8 and grade < 0.9:
        score = "a B"

    # If the number is greater than or equal to 0.7 and less than 0.8 the grade is a "C"
    elif grade >= 0.7 and grade < 0.8:
        score = "a C"

    # If the number is greater than or equal to 0.6 and less than 0.7 the grade is a "D"
    elif grade >= 0.6 and grade < 0.7:
        score = "a D"

    # If the number is less than 0.6 the grade is an "F"
    elif grade < 0.6:
        score = "an F"

        # Print "Your grade is a <grade>"
        print ("Your grade is {}".format(score))
