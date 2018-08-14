## Day 5 Exercise 1 - Caps

# Write a program that prompts for a file name, then opens that file 
# and reads through the file, and print the contents of the file in 
# upper case. Use the file words.txt

def upper_and_overwrite(file_read,file_write):
    with open(file_read,'r') as file_read, open(file_write,'w') as file_write:
        for line in file_read:
            print(line.upper(),file=file_write, end='')

upper_and_overwrite('words.txt','new_words.txt')
 

#def upper_file(filename, end ="\n"):
#    list1 =[]
#    with open(filename,'r') as open_file:
#        for line in open_file:
#            list1.append(line.upper())
#        return list1
 
#upper_list = (upper_file('words.txt', end = "\n"))


# Now write the program to output the caps version of the file 
# into a new file. 

#def overwrite(filename,line_list):
#    with open(filename,'w') as open_file:
#        for line in line_list:
#            print(line.upper(), file=open_file, end ='')

#y = overwrite('new_words.txt',upper_list)

