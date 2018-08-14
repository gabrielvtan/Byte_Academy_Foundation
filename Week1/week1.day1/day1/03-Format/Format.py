#* Store 3 and 'little pigs' in two variables. Print the string "The 3 little 
# pigs" using those 2 variables.

a = 3
b = 'little pigs'
print ("The {} {}".format(a,b))

# Store the number 6.7 in a variable, then make it print as 6.700

c = 6.7
print("{:.3f}".format(c))

# Store the strings "Sam" and "Josephine" into variables. 
# Print the text
#* Where each name and the extra black space 
# combine to 12 characters wide.

d = 'Sam'
e = 'Josephine'
print('The joint account for {:<12} and {:<12}'.format(d,e), 'has $1000.') 

# * Do the same, but make the names display all the way to the 
# right of the twelve spaces.

print('The joint account for {:>12} and {:>12}'.format(d,e), 'has $1000.')