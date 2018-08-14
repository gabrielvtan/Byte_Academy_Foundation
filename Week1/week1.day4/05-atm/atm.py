#check for user input
def user_input():
    while True:
        command = input("What would you like to do: C, W, D, Q?\n")
        if command in "CWDQ":
            break
    if command == 'C':
        check_balance()
    elif command == 'W':
        withdraw()
    elif command == 'D':
        print('return deposit()')
    else:    
        return


#function for check balance
def check_balance():
    print('Your current balance is {:.2f}.\n'.format(balance))
    while True: 
        command = input("What would you like to do: W, D, Q? \n")
        if command in "WDQ":
            break
    if command == 'W':
        withdraw()
    elif command == 'D':
        return deposit()
    else:
        return
 
#function for withdrawal
def withdraw():
    global balance
    print('Your current balance is {:.2f}.\n'.format(balance))
    withdrawal = float(input("How much would you like to withdraw: \n"))
    if withdrawal > balance:
        print("Your withdrawal request is greater than your balance.\n")
        withdraw()
    elif withdrawal>0:
        balance = balance - withdrawal
        print("You have withdrawn {} dollars.\nYour remaining balance is {} dollars. \n".format(withdrawal, balance))
            

#function for deposit
def deposit():
    global balance
    print('Your current balance is {:.2f}.\n'.format(balance))
    deposit = float(input("How much would you like to deposit: \n"))
    if deposit >0:
        balance = balance + deposit
        print("You have deposited {} dollars.\nYour total balance is {} dollars. \n".format(deposit, balance))

 
# Global Variables
balance = 1000.00
user_input()

