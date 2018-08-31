# Class Basics
# Classes can be very useful for storing complicated objects with their own methods and variables.
# Defining a class is much like defining a function, but we use the class keyword instead. 
# We also use the word object in parentheses because we want our classes to inherit the object class. 
# his means that our class has all the properties of an object, which is the simplest, most basic class. 
# Later we'll see that classes can inherit other, more complicated classes. 
# Classes can have member variables that store information about each class object
# We call them member variables since they are information that belongs to the class object
# Objects created within a class inherit the attributes of a the class
# There is a special function named __init__() that gets called whenever we create a new instance of a class. 
# It exists by defualt and we overwrite the default version inorder to provide more input variables
# The first argument passed to __init__ must always be the keyword self - this is how the object keeps track
# of itself internally - but we can pass additional variables after that
# You don't need to include the self keyword when you create an instance of a class, because self gets added 
# to the beginning of your list of inputs automatically by the class definition
# We use dot notation to access the member variables of classes since those variables belong to the object
# Besides member variables, classes can also have their own methods
# We can modify variable that belong to a class the same way that we initialize those member variables.
# This can beuseful when we want ot change the value a variable takes on based on something that happens 
# inside of a class method

class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg = mpg
   
  def display_car(self):
    print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))
    
  def drive_car(self):
    self.condition = "used"

class ElectricCar(Car):
  def __init__(self, model, color, mpg, battery_type):
    self.model = model
    self.color = color
    self.mpg = mpg
    self.battery_type = battery_type
  
  def drive_car(self):
    self.condition = "like new"

my_car = ElectricCar("Tesla", "red", "200", "molten salt")

print(my_car.condition)
my_car.drive_car()
print(my_car.condition)

# One useful class method to override is the built-in __repr__() method, which is short for representation; 
# by providing a return value in this method, we can tell Python how to represent an object of our class
class Point3D(object):
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    
  def __repr__(self):
    return ("({}, {}, {})".format(self.x, self.y, self.z))
    
my_point = Point3D(1, 2, 3)
print (my_point)
