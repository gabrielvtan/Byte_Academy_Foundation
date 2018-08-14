## Day 3 Challenge 01 - Matrix Calculations

#### Do this first part even if you can't figure out the challenge

* Try out the following code:

```python
from random import randint

print(randint(0,99))
print(randint(100,1000))
print(randint(1,2))

# Unlike most other ranges, randint does contain its maximum. So randint(1,10) can result in a 10
# why did they do that? it's inconsistent! Beats me.
```

* Now use a for loop to build a 10 element list of random integers

* Use core python functions to find the minimum, maximum, and sum of the numbers

#### Challenge Part 1

* We're going to build a matrix and do some calculations

* First write code that generates a 3 x 3 list of lists where each element is a number between 0 and 9

* * You may want to solve the problem of just generating a list of 3 random numbers first and then figure
out how to build a square.

* Write code that prints it out

* Now add variables ```width=5``` and ```height=4``` to the top of your code. Change your matrix building
loop and print loop to work with the variable parameters

* Now calculate the sum of each row and output them as a verticle arrangement as tall as your matrix was

#### Challenge Part 2

* Sort the matrix by their row sums, so the row with the lowest sum is at the top and the row with the biggest sum is at the bottom

* Now do it by their column sums.

#### Open ended challenge

* This is for students with a background in mathematics, specifically linear algebra

* Generate two matricies and add them together

* Generate two different matricies and multiply them together

* Calculate the determinant