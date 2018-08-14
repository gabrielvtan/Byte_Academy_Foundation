## Day 4 Exercise 1 functions and values

# There is nothing to turn in for this exercise

# What is the result of this program?:


def double(x):
    return x * 2

print(double(5))


#What are the outputs of this program:




def different_double(x):
    x = x * 2
    return x

a = 5
print(different_double(a))
print(a)

x = 5
print(different_double(x))
print(x)

different_double(x)
print(x)



# Do you understand the results of this? Do you understand the difference between 'print' and 'return?'

# Do you think it's better for most functions to use return or to use print?


def pdouble(x):
    x = x * 2
    print(x)

def rdouble(x):
    x = x * 2
    return x

w = 5
x = pdouble(w)
print(x)


w = 8
y = pdouble(pdouble(w))
print(y)

w = 3
x = rdouble(w)
print(x)

w = 7
y = rdouble(rdouble(w))
print(y)


#What is the result of this?


def dmult(x, y=2):
    x = x * y
    return x

print(dmult(5))
print(dmult(5, 3))

