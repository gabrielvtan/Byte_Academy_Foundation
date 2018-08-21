## Nested for loops -  Matrix Transpose
#### Group or solo work
# You may work alone or in a group on this project
#### Requirements
# You are going to read a matrix of numbers from a file
# Construct a two dimensional list of the values
# Create a new two dimensional list where the rows are the columns and the columns are the rows
# Output that to a new file
import re


file = 'number1.txt'

def open_file(filename):
    with open(filename,'r') as file_object:
        output_list = []
        for line in file_object:
            output_list.append(line.split())
    return [*zip(*output_list)]

zip_list = open_file(file)

def write_file(filename, line_list ):
    with open(filename, 'w') as file_object:
        for line in line_list:
            print("  ".join(line), file = file_object)

write_file('number1.txt', zip_list)

#### example:


#1  2  3  4  5
#6  7  8  9  10


#will be transformed into

#1  6
#2  7
#3  8
#4  9
#5  10

