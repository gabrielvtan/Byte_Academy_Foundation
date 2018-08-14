"""

def f(a):
    a = a + 1
    return a

f(2) # does nothing on its own
result = f(3) # return value is stored in an assignment statement
print(result)

# to immediately output the return value of a function:
print(f(7))
# but remember that that value won't be saved anywhere

a = 10
b = f(a)
print(a) # f doesn't change a, even though it has its own variable called a
print(b)


def pf(a):
    a = a + 1
    return a

b = pf(20)
print(b)

c = pf(pf(1)) # an error
print(c)

def say_number(number):
    return "The number is {}".format(number)

def quote(string):
    return "They said \"{}.\"".format(string)

print(say_number(5))
print(quote('hello'))

print(quote(say_number(17)))

"""

d = "message"

def three_vars(a, b, c):
    global d # use this
    print(d)
    d = "new message"
    return "a: {}, b: {}, c: {}".format(a, b, c)

a = 'A'
b = 'B'
c = 'C'
print(three_vars(b, c, a))
