## Day 5 Exercise 2 - Processing Files
#### Extracting data
#Write a program that prompts for a file name, then opens that file and 
# reads through the file, looking for lines of the form:

#X-DSPAM-Confidence:    0.8475

#Count these lines and extract the floating point values from each of the 
# lines and compute the average of those values and produce an output as 
# shown below. 
# Do not use the sum() function or a variable named sum in your solution.
#### Hint
# Don't write it all at once. First just find the lines, 
# then isolate the numbers, then do the math.

file = 'mbox-short.txt'
# function to search file for key
def search_sum(file_read):
    output_list = []
    with open(file_read, 'r') as file_read:
        for line in file_read:
            if 'X-DSPAM-Confidence:' in line:
                output_list.append(line)
    return output_list

lines = search_sum(file)

#isolate numbers
strip_lines = [i.strip('X-DSPAM-Confidence: ') for i in lines]
strip_lines = [i.strip('\n') for i in strip_lines]

#convert to float, find sum, and average
float_list = [float(i) for i in strip_lines]

sum=0
for i in float_list:
    sum = sum + i
    
print(sum/len(float_list))







