## Foundation Week 2 Day 3 - Regular Expressions
import re

#### Basics
# Name a yellow food that this regular expression will match ```"[abn]+"```
print(re.search("[abn]+", "banana"))

# Write a sentence that this regular expression will match ```"^Once.*end\.$"```
print(re.search("^Once.*end\.$","Once.end."))

# Write a similar sentence that the expression won't match.
print(re.search("^Once.*end\.$","Wont.match."))

# If a name record has to have a first name and a last name, separated by
#and each beginning with a capital letter, write an expression that matches
#this and excludes non-matching records.
""" This does not work for Jackie O"""
print(re.search("^[A-Z][a-z]+\s[A-Z]([A-Za-z]+$)", "John Adams"))

# Write an expression that matches "[timestamp: 123456]" 
# where 123456 can be any integer. Include the [ and ] in the string 
# to be matched.

print(re.search("(?<![\w\d])[timestamp: [0-9]+](?![\w\d])","[timestamp: 123456345345435345]"))

# Write an expression that matches a string that is exactly the equals 
# sign twenty times.
#====================
print(re.search("(?<![\w\d])={20}(?![\w\d])","===================="))

# Write an expression that matches an email address. NAME@SERVER.TLD 
# where NAME can be any combination of letters, numbers, dashes, and dots, 
# SERVER follows the same rules as NAME and TLD is three lowercase letters 
# (like com or edu)
print(re.search("[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+\.[a-z]{3}","gabriel.v.tan@gmail.com"))

# Now write a function that takes a string and returns None if it is 
# not an email address in it and returns just the address if there is 
# an email address in it.

string = "My name is Carter and my email address is carteradams@gmail.com"
def find_email(string):
    expression = "[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+\.[a-z]{3}"
    match = re.search(expression, string)
    if match is None:
        return None
    else:
        return match
 
# Write an expression that can find time expressed like 12:00
print(re.search("([0-9]{1,2}:[0-9]{2})","The time is 12:12pm"))