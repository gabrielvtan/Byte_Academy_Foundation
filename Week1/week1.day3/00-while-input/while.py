## Day 3 Exercise 0.

# Ask the user to input integers or 'done', if they print an integer print that integer converted to a float
#with 2 0's after the decimal point (remember format?)

# If they type done exit the program

# Know how to do this two different ways

# * Using while True and a break statement

while True:
    inp = input("give me an integer: ")
    if inp == 'done':
        break
    else:
        print("{:.2f}".format(float(inp)))


# * Setting an input variable outside the loop and using a test with while.
inp = input("give me an integer: ")
while inp != 'done':
    print("{:.2f}".format(float(inp)))
    inp = input("give me an integer: ")


# Now finish any exercises from yesterday that needed while that you still need to do.