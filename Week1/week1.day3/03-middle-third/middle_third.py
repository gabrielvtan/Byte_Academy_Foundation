## Day 3 Exercise 3 - Middle Third

#Write a program that gets a string input from a user and then prints how many characters long the
#string is and then prints the middle third.
#the middle third of it.
string = input("Give me string: ")
print(len(string))
section = int(len(string)/3)
section1 = section*1
section2 = section*2
print(string[section1:section2])



# For instance
#Input a string: Now is the time for all good men to come to the aid of their country
#68
#l good men to come to 
