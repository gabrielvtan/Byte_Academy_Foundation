## Process File Revisited

# Do Day 5 Exercise 2 again, but this time use a regular expression to 
# see if the a line matches and to extract the string of the floating 
# point number.

## Day 5 Exercise 2 - Processing Files

#### Extracting data

#Write a program that prompts for a file name, then opens that file 
# and reads through the file, looking for lines of the form:

#X-DSPAM-Confidence:    0.8475

#Count these lines and extract the floating point values from each 
# of the lines and compute the average of those values and produce an 
# output as shown below. Do not use the sum() function or a variable 
# named sum in your solution.

#### Hint

# Don't write it all at once. First just find the lines, then isolate 
# the numbers, then do the math.

import re

file = 'mbox-short.txt'
 
def search_string(filename):
    expression = "(?<=X-DSPAM-Confidence: )0\.\d+"
    with open(filename, 'r') as open_file:
        data = re.findall(expression, open_file.read())
    return data


def find_sum(data):
    sum = 0 
    for num in data:
        sum += float(num)
    return sum /len(data)
 


print (find_sum(search_string(file)))



 