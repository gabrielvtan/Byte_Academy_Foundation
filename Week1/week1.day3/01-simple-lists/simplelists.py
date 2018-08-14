# Day 3 - Exercise 1 Simple Lists

# Input a string, using a while loop to make the user enter new strings until the length is at least 5.
# Print the 5th character, otherwise print "It's short, but the last character is <>" where <> is the last character in the string.

while True:
    string = input("give me a 5 character string: ")
    if len(string) < 5:
        print("It's short, but the last character is {}".format(string[-1]))
    else:
        print("The fifth character is {}".format(string[4]))
        break


# Use slice indexing ([a:b:c] possibly with some of the values missing) to store a string that is just
#every second character.
a = list(string)

# Convert the string to a list, store it in a new variable called list1
list1 = (a[1::2])

# Do the exact same thing and store it in list2
list2 = (a[1::2])

# Print the boolean result of list1 == list2
print(list1 == list2)

# Print the boolean result of list1 is list2
print(list1 is list2)

# Print a string that in your own words explains what is going on.
print("The '==' operator checks to see if the values are equivalent, while 'is' checks to see if the addresses of the data are equivalent")

# Add '!' to the end of the list.
a.append('!')
print(a)

# put this line: ``` list3 = list1 ```
list3 = list1

# store the new list [1, 2, 3] in the first element of list1 (overwrite the existing element)
list4 = [1,2,3]
list1[0] = list4

# print the boolean value of ``` list1 == list3 ```
print(list1 == list3)

# print the boolean value of ``` list1 is list3 ```
print(list1 is list3)

# print list1
print (list1)

# print list3
print(list3)

# print a string that in your own words explains what is going on
print("list1 and list3 have equivalent data points and addresses due to the assignment of 'list3 = list1'")

# print the index of the '!'
new = (a.index('!'))
print(new)

# using for in, build a copy of list1 one element at a time.
new_list1 = []
for x in list1:
    new_list1.append(x)
print(new_list1)

# using an index value, a range, and a for statement, print each element of the list on its own line
for y in range(len(new_list1)):
    print(new_list1[y])