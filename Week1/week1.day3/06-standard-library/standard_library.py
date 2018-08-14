## Day 3 Exercise 6 - Standard Library

# You don't have to turn in anything, but you might want to make notes for future reference.

#### Documentation exercise

# This is an exercise in looking up documentation. It should all be here: [https://docs.python.org/3/library/stdtypes.html#common-sequence-operations]

# Input a string.
string = input("Give me a string: ")

# Save a conversion of the string into a list in another variable.
list1 = list(string)
print(list1)

# Print the list reversed without changing what's stored in the variable.
list2 = (list1[::-1])
print(list2)

# Now actually reverse it. Print the changed variable out.
list2 = ''.join(list2)
print(list2)

# With one line of code, remove the last element of the list and store it in a variable.
last = list2[-1]
print(last)

# Print the string capitalized.
print(list2.upper())

# Write if statements that test if the string is all alphanumeric characters (what does that mean?) write a test to see if it is a string of a number
if list2.isalnum():
    print("TRUE")
else:
    print("FALSE")

# Print out the string repeated 3 times
print(list2 * 3)

# Replace all the 'e's in the string with 'i's and save it to the original variable.
string = list2.replace('e','i')
print(string)

# Print the string converted to a UTF-8 bytes object
string_byte = (string.encode('utf-8'))
print(string_byte)

# Print the alphabetically last letter in the list.
string_byte = list(string_byte)
last_letter = (max(string_byte))
last_index = string_byte.index(last_letter)
print(string[last_index])

# Sort the list so the characters are in alphabetical order
list1.sort()
print(list1)

# Convert the list into a tuple
print(tuple(list1))