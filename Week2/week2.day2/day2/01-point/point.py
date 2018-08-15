## Foundation Day 2 Exercise 1

# Write a class called Point
# It has two attributes, x and y
# p = Point should create an object with x and y equal to 0
# create a method called display() that prints "Point: (<x>, <y>)"
# where x and y are the attributes

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def display(self):
        print("Point: ({}, {})".format(self.x,self.y))

p = Point(0,0)
p.display()
 