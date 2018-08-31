# A basic class consists of the class keyword, the name of the class and the class from
# which the new class inherits in parentheses
# __init__() is used to initialize objects it creates and always takes at least one
# argument (self) which refers to the object being created

class Fruit(object):
  """A class that makes various tasty fruits."""
  def __init__(self, name, color, flavor, poisonous):
    self.name = name
    self.color = color
    self.flavor = flavor
    self.poisonous = poisonous

  def description(self):
    print ("I'm a {} {} and I taste {}.".format(self.color, self.name, self.flavor))

  def is_edible(self):
    if not self.poisonous:
      print ("Yep! I'm edible.")
    else:
      print ("Don't eat me! I am super poisonous.")

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()

# We can access attributes of our objects using dot notation
class Square(object):
  def __init__(self):
    self.sides = 4

my_shape = Square()
print my_shape.sides #4

class Animal (object):
  def __init__(self, name):
  	self.name = name

zebra = Animal("Jeffrey")
print (zebra.name) # "Jeffrey"

# Class definition
class Animal(object):
  """Makes cute animals."""
  # For initializing our instance objects
  def __init__(self, name, age, is_hungry):
    self.name = name
    self.age = age
    self.is_hungry = is_hungry

# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print (zebra.name, zebra.age, zebra.is_hungry)
print (giraffe.name, giraffe.age, giraffe.is_hungry)
print (panda.name, panda.age, panda.is_hungry)

#Class Scope
# The scope of a variable is the context in which it's visible to the program
# When dealing with classes, you can have variables that are available everywhere (global variables)
# variables that are only available to members of a certain class (member variables), and
# variables that are only available to particular instances of a class (instance variables)

# Methods
# When a class has its own functions, those functions are called Methods
class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print(self.name)
    print(self.age)
    
hippo = Animal("Hippy", 5)
hippo.description()

# More practical application of Classes 
class ShoppingCart(object):
  """Creates shopping cart objects
  for users of our fine website."""
  items_in_cart = {}
  def __init__(self, customer_name):
    self.customer_name = customer_name

  def add_item(self, product, price):
    """Add product to the cart."""
    if not product in self.items_in_cart:
      self.items_in_cart[product] = price
      print (product + " added.")
    else:
      print (product + " is already in the cart.")

  def remove_item(self, product):
    """Remove product from the cart."""
    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print (product + " removed.")
    else:
      print (product + " is not in the cart.")

my_cart = ShoppingCart("Gabby")
my_cart.add_item("Toilet paper", 2)

# Inheritance
# This is the process by which one class takes on the attributes and methods of another, 
# and it's used to express an is-a relationship
class Customer(object):
  """Produces objects that represent customers."""
  def __init__(self, customer_id):
    self.customer_id = customer_id

  def display_cart(self):
    print ("I'm a string that stands in for the contents of your shopping cart!")

# We are setting class ReturningCustomer to inherit the class from Customer
class ReturningCustomer(Customer):
  """For customers of the repeat variety."""
  def display_order_history(self):
    print ("I'm a string that stands in for your order history!")

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()

# Overriding Inheritance
class Employee(object):
  def __init__(self, name):
    self.name = name
  def greet(self, other):
    print "Hello, %s" % other.name

class CEO(Employee):
  def greet(self, other):
    print "Get back to work, %s!" % other.name

# In this example, the method of Employee is being passed to greeting the CEO through the 
# use of emp.greet(ceo)
ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo)
# Hello, Emily
ceo.greet(emp)
# Get back to work, Steve!

# On the flip side, sometimes you'll be working with a derived class (or subclass) and realize that you've 
# overwritten a method or attribute defined in that class' base class ( also called a parent or superclass)
# that you actually need. This is accomplished by using 'super'
# in this example, 'super' is being used to refernce back to the parent's method of calculate wages
class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00
  
  def full_time_wage(self, hours):
    return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee('Milton')
print (milton.full_time_wage(10))

# Putting it all together
class Triangle(object):
  number_of_sides = 3
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
    
  def check_angles(self):
    if (self.angle1 + self.angle2 + self.angle3) == 180:
      return True
    else:
      return False

my_triangle = Triangle(90,30,60)
print(my_triangle.number_of_sides)
print(my_trinagle.check_angles())

class Equilateral(Triangle):
  angle = 60
  def __init__(self):
    self.angle1 = self.angle
    self.angle2 = self.angle
    self.angle3 = self.angle