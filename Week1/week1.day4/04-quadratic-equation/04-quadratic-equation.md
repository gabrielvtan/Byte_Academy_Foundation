## Day 4 Exercise 4 - Parabolas and Quadratic Equation

[https://en.wikipedia.org/wiki/Quadratic_formula]

* A quadratic polynomial is an equation of x of the form y = a * (x ** 2) + b * x + c.

* First write a function that takes 4 inputs: x, a, b, and c and returns a y

* * like ```parabola(x, a, b, c):```

* Now write a function that takes 4 inputs: a list tuple of floats (x values), a, b, and c and returns a list of y values

* * like ```parabola_list(xlist, a, b, c):``` 

#### solving for y = 0

* The points on the parabola where y = 0 are given by:

(-b +/- (the square root of b**2 - 4 ac)) divided by 2 (see the wikipedia link for better documentation)

* * At the +/- o add to find the first root and subtract to find the second.

* Write a function that takes 3 inputs (a, b, c) and returns the two values of x where y = 0. Return them as a 2 element tuple.

* * like ```solutions(a, b, c)```

* * ```from math import sqrt``` might be useful  

#### Interactive testing

* Import your python file as a module in the repl. To do this, be in the same directory as your file and then in the interactive environment, type import answer (if your filename is answer.py)

* * If it prints output after importing, move your test code into an ```if __name__ == "__main__":``` block at the end of the file.

* Try out some different values for your three functions interactively. Then try this:

```python
a = 1
b = 0
c = -4
zeros = answer.solutions(a, b, c)
y_vals = answer.parabola_list(answer.solutions, a, b, c)
print(y_vals)
```

* * you may have to change the names to your names for the module and functions

#### Bigger projects

* As the size of your projects grows, a good way to test your work as you build it is to break the problem into small functions and import your work in the interactive environment to test each function.

* A useful feature is the reload function from the 'imp' module

```python
from imp import reload
import mymodule

# test functions in mymodule

# make some changes to the file

reload(mymodule)

# test the changes

# and so on
```
