## Foundation Week 2 Day 2 Exercise 2
# Distance function
# take your Point class from the previous exercise and add a new method:
# Point.distance(p) where p is another point that returns a floating point
# value for the distance between the two points
# if one point is (x1, y1) and another point is (x2, y2) then the formula
# for distance is math.sqrt((x1 - x2) `**` 2 + (y1 - y2) `**` 2)
import math

class Point():
    """ point class for representing and manipulating x,y coordinates """

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distance(point1, point2):
        xdiff = point2.getX() - point1.getX()
        ydiff = point2.getY() - point1.getY()

        dist = math.sqrt(xdiff ** 2 + ydiff ** 2)
        return dist

point1 = Point(0,0)
point2 = Point(3,4)

print(Point.distance(point1, point2))
