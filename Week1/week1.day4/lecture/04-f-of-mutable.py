"""
def f(x):
    x = x + 10

x = 5
f(x)
print(x)
print(f(x))

quit()

def f2(a_list):
    a_list[0] = "New Value"

def new_len(a_list):
    return len(a_list)

li = ['a', 'b', 'c']
f2(li)
print(li)

quit()
"""

def f3(a_list):
    a_list = ['entirely', 'new', 'list'] 


li = ['a', 'b', 'c']
f3(li)
print(li)