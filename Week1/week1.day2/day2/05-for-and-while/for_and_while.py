## Day 2  Exercise 5 - for and while

# Write a program that inputs an integer from the user and then prints the numbers from 0 to that integer (including that integer).
first = int(input("Give me an integer! "))
for x in range (first +1):
    print(x)

# Now make it input a second integer and print every even number from 0 until the given number.
second = int(input("give me a second integer! "))
for y in range (0, second +1, 2):
    print(y)

# Write this program using both a step value for range and using an if test with % inside your loop.