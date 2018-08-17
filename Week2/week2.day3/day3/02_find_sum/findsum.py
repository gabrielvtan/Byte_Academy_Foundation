#Finding Numbers in a Haystack
#In this assignment you will read through and parse a file with text and 
# numbers. You will extract all the numbers in the file and compute the sum 
# of the numbers. The numbers can appear anywhere in the line. 
#There can be any number of numbers in each line (including none).

#Desired output:

#regex_sum.txt : 445833<br/>
#regex_sum_1.txt : 466318

import re

file = 'regex_sum_1.txt'

def open_and_create_string(filename):
    with open(filename, 'r') as open_file:
        data = open_file.read()
        return data

def find_sum(file):
    match = re.findall("\d+", open_and_create_string(file))
    match = list(map(int,match))
    return sum(match)


print(find_sum(file))
 