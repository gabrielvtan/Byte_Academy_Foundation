## Day 2 - Exercise 6 - While Input

# Write a program that asks a user to input an integer, and keeps asking the user to input integers until they input 'done'
integer = ""
list = []

while integer is not "done":
    try:
        integer = int(input("Give me an integer! "))
        list.append(integer)
    except:
        integer == "done"
        break

# Afterward print the sum and the average of those numbers
print (list)
print("sum is {}".format(sum(list)))
print("average is {}".format((sum(list))/len(list)))

