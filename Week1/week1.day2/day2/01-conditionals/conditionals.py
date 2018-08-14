# Use input() to prompt the user to enter an integer and use int() to convert the string 
# to an integer value. Store the result in a variable.
integer = int(input("Enter an integer: "))

# If the number is equal to zero, print "It is zero!" If it is not, print "It's not zero!"
if integer == 0:
    print("It is zero!")
else:
    print("It is not zero!")

# If the number is less than 10 print "Less than 10!" If it's greater than 10 and it is 
# less than 20 print "Less than 20!" Otherwise, print "Big number you got there!
# " Use one 'if' one 'elif' and one 'else.'10
if integer < 10:
    print("Less than 10!")
elif 10 < integer < 20:
    print("Less than 20!")
else:
    print("Big number you got there!")

# If the number is greater than or equal to 0 and less than but not equal to 100, 
# print it out using .format() so it is always two digits (03 for 3 for instance)
if integer >= 0 and integer < 100 :
    print ("{:.2f}".format(integer))

# If the number is even print "It is even!"
if (integer % 2) == 0:
    print ("It is even!")

# If the number is divisible by 5 print "It is divisible by five!"
if (integer % 5) ==0:
    print("It is divisible by five!")

# If a number is divisible by 13 or it is divisible by 17, print "Cicadas!"
if (integer % 13 == 0) or (integer % 17 == 0):
    print("Cicadas")

# If the number is both even and divisible by 5 print "It is both even and divisible by 5!" 
# (Don't just check for divisibility by 10)
if (integer % 2 == 0) and (integer % 5 == 0):
    print("It is both even and divisible by 5!")

# If you answered the last question1 using 'and' answer it with an if statement inside of 
# an if statement. If you answered the last question using a nested if, answer it with 'and'
if (integer % 2 == 0):
    if (integer % 5 == 0):
        print("It is both even and divisible by 5! - Part Deux")

# If the number is not divisible by seven, update the variable by multiplying it by 7. 
# Otherwise divide it by 2. After updating the number, print "The new number is <number> now."
if ((integer % 7) is not 0):
    integer = integer*7
    print("The new number is {} now".format(integer))
else:
    integer = integer/2
    print("The new number is {} now".format(integer))


# Be sure to test each possibility.