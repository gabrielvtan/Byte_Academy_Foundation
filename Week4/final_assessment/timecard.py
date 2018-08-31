import json
import time

mastertimecard = 'timecard.json'

def user_input():
    print("Hello human employee, please enter your Employee ID.")
    userAccount = int(input('Employee ID: '))
    pin = int(input('PIN: '))
    accounts = read_file()    
    new_account = {}
    if userAccount == 0 and pin == 0:
        boss_view(userAccount)
    else:
        if str(userAccount) in accounts:
            if pin == (accounts[str(userAccount)]['PIN']):
                main_timestamp(str(userAccount), accounts[str(userAccount)]['PIN'], accounts[str(userAccount)]['Time'])
            else:
                print("You have entered an incorrect pin number.")
                user_input()
        else:
            accountKey = str(userAccount)
            new_account = {
                    "PIN" : pin,
                    "Time" : 0
            }
            accounts[accountKey] = new_account
            write_file(accounts)
            print("Thank you for opening a new account!\n")
            user_input()

def read_file():
    with open(mastertimecard, 'r') as jsonfile:
        accounts = json.load(jsonfile)
        return accounts

def write_file(accounts):
    with open(mastertimecard, "w") as jsonfile:
        json.dump(accounts, jsonfile)

def main_timestamp(userAccount, pin, time):
    print("Hello Employee: {}".format(userAccount))
    new_time = input("How much time did you work today (HH:MM): ")
    hours, minutes = new_time.split(':')
    total_minutes = int(hours)*60 + int(minutes)
    if total_minutes > 0:
        time = time + total_minutes
        print("You have entered {} minutes.\nYour total work time is {} minutes".format(total_minutes, time))
        print('Thank you! Have a great day!')
        update_masterfile(userAccount, pin, time)

def boss_view(userAcccount):
    accounts = read_file()
    header = 'EMPLOY  ID           MINUTES WORKED'
    boarder = '-----------------------------------'
    print("Boss View")
    print(boarder)
    print(header)
    print(boarder)
    for employee in accounts:
        print("{:<20} {:<20}".format(employee, accounts[employee]["Time"]))
    print(boarder)
    
# Update the file whenever a user enters in a new time
def update_masterfile(userAccount, pin, time):
    accounts = read_file()
    accounts[str(userAccount)]['Time'] = time
    write_file(accounts)

user_input()