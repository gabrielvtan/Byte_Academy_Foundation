import json
import os

masterfile = 'accounts.json'

def user_input():
    userAccount = int(input('Account Number: '))
    pin = int(input('PIN: '))
    accounts = read_file()
    new_account = {}
    if str(userAccount) in accounts:
        if pin == (accounts[str(userAccount)]['PIN']):
            main_atm(str(userAccount), accounts[str(userAccount)]['PIN'], accounts[str(userAccount)]['Balance'] )
        else:
            print("You have entered an incorrect pin number.")
            user_input()
    else:
        accountKey = str(userAccount)
        new_account = {
                "PIN" : pin,
                "Balance" : 0
        }
        accounts[accountKey] = new_account
        write_file(accounts)
        print("Thank you for opening a new account!")
        user_input()
        

def read_file():
    with open(masterfile, 'r') as jsonfile:
        accounts = json.load(jsonfile)
        return accounts

def write_file(accounts):
    with open(masterfile, "w") as jsonfile:
        json.dump(accounts, jsonfile)

# Open user account file and check if account already exists
def main_atm(userAccount, pin, balance):
    while True:
        print("C - Check Balance\ncW - Withdraw\nD - Deposit\nQ - Quit")
        command = input("Welcome Account: {} What Would you like to do?\n". format(userAccount))
        if command in "CWDQ":
            break
    if command == 'C':
        check_balance(userAccount, pin, balance)
    elif command == 'W':
        withdraw(userAccount, pin, balance)
    elif command == 'D':
        deposit(userAccount, pin, balance)
    elif command == 'Q':
        print('Thank you! Have a great day!') 
    
    # NEED TO ADD OS.CLEAR TO MAKE THE INTERFACE PRETTIER

def check_balance(userAccount, pin, balance):
    print('Your current balance is {:.2f}.\n'.format(balance))
    while True:
        print("W - Withdraw\nD - Deposit\nQ - Quit") 
        command = input("What would you like to do: W, D, Q? \n")
        if command in "WDQ":
            break
    if command == 'W':
        withdraw(userAccount, pin, balance)
    elif command == 'D':
        return deposit(userAccount, pin, balance)
    elif command == 'Q':
        print('Thank you! Have a great day!') 
        

def withdraw(userAccount, pin, balance):
    print('Your current balance is {:.2f}.\n'.format(balance))
    withdrawal = float(input("How much would you like to withdraw: \n"))
    if withdrawal > balance:
        print("Your withdrawal request is greater than your balance.\n")
        withdraw(userAccount, pin, balance)
    elif withdrawal>0:
        balance = balance - withdrawal
        print("You have withdrawn {:.2f} dollars.\nYour remaining balance is {:.2f} dollars. \n".format(withdrawal, balance))
        print('Thank you! Have a great day!')
        update_masterfile(userAccount, pin, balance)
        

def deposit(userAccount, pin, balance):
    print('Your current balance is {:.2f}.\n'.format(balance))
    deposit = float(input("How much would you like to deposit: \n"))
    if deposit >0:
        balance = balance + deposit
        print("You have deposited {} dollars.\nYour total balance is {} dollars. \n".format(deposit, balance))
        print('Thank you! Have a great day!')
        update_masterfile(userAccount, pin, balance)
        

# When Quit is selected, the 
def update_masterfile(userAccount, pin, balance):
    accounts = read_file()
    accounts[str(userAccount)]['Balance'] = balance    
    write_file(accounts)

# Start the program 
user_input()


    