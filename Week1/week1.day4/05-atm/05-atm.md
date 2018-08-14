## Day 5 Exercise 5 - ATM

#### Time for something bigger

* You are going to make an ATM

* The user will be presented with a list of options

```
C - check balance

W - withdrawal

D - deposit

Q - quit
```

* They input the value and then are shown their balance, given a prompt for how much to withdraw, or how much to deposit. If they try to withdraw more money than they have, they get an error. Then they see the list of options again and it exits.

* The balance should begin at 1000.00 and update after each input. That is, if I withdraw 500.00 and then check my balance, it should reflect the new total.

* There whould be (at least) a check_balance, withdraw, and deposit function. You will probably be calling them from inside an if statement with multiple elifs all inside a while loop.

* One of the challenges is going to be having each function know the value of the balance. There are a few ways to accomplish this, one of which is to use the ``` global ``` keyword with a variable defined outside of the function.

* * Global variables are very unpopular with programmers. They make for a big mess when programs get large. There is a better solution that uses classes and objects, and we'll come back to this.
