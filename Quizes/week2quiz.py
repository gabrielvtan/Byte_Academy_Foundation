## Week 2 Foundations Quiz
import re

string = "Jenny, don't change your number 867-5309"
string1 = "555-4321? That sounds fake"
string2 = "My number is 12-8930"
string3 = "212-893 is my number."

# Write a function, ```phone`_`number(string)```
# * Takes one argument, a string
# * Returns a True or False value (or a value equivalent to True or False)
# * Does not print or input
# * Returns True if the string contains a phone number of the form 555-5555

def phone_number(string):
    expression = "[0-9]{3}-[0-9]{4}"
    match = re.search(expression, string)
    if bool(match) == True:
        return True
    else:
        return False

print(phone_number(string))
print(phone_number(string1))
print(phone_number(string2))
print(phone_number(string3))







#### Test Strings:

##### should match (return a True value):

# "Jenny, don't change your number 867-5309"

#and

# "555-4321? That sounds fake."

##### should not match (return a False value):

# My number is 12-8930

#or

# 212-893 is my number.

#### Submissions:

# Upload your code to github and send me a link. It can either be in an existing repository or a new one.
