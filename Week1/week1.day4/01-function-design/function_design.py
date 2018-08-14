## Day 4 Exercise 1 Function Design

#### Write the following functions. Pick descriptive names for the functions and their parameters.

# A function that returns True if a number is divisible by 7 and False if it does not.
def func1(x):
    return x % 7 == 0
y=func1(8)
print(y)

# A function that returns True if a string is 10 characters or longer and False if it does not.
def func2(x):
    return len(x) >= 10
y = func2('thisismorethan10')
print(y)

# A function that returns the first letter of a string
def func3(x):
    return x[:1]
y = func3('string')
print(y)


# A function that takes an integer and returns a list with that many elements, where every element is zero.
def func4(x):
    return [ 0 for i in range(x) ]
y = func4(7)
print(y)

# A function that takes a list as input and prints out the contents of each element on a numbered line, like:
##print_list(['a', 'bee', 'cee', None])
#1. a
#2. bee
#3. cee
#4. 'None'
def func5(x):
    for i in range(len(x)):
        print (i, x[i])
y = func5(['a','b','c','d','e'])

# A function that takes a string as input and returns a list of two character segments of the string like:
#segment('Carter Adams')
#returns
#['Ca', 'rt', 'et', ' A', 'da', 'ms']
def func6(x,y):
    return[y[i:i+x] for i in range(0,len(y),x)]
z = func6(2,'Carter Adams')
print(z)

# A function that when given an integer prints out that many dash charactes between two +'s, so dashprint(5) would print '+-----+' 
# make sure the print ends in a new line.
# * This function should print, and not have any return value.
def func7(x):
    print('+{}+\n'.format('-'*x))
y = func7(7)

# A function that takes a string, and then uses that string as the prompt text for an input. Repeat the prompt as long as the input is not an integer. 
# Return the integer (as an integer) when it is one.
def func8(x):
    x = input("Give me an integer: ")
    if not x.isdigit():
        return(func8(x))
    else:
        return(x)


# A function that takes two integers, one that represents a width and one that represents a height, and returns a new two dimensional array,
#  where each element is None
def func9(w,h):
    return[None, None]


