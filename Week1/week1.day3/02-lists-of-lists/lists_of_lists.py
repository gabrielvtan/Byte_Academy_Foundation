## Day 3 Exercize 2 Lists of lists

#copy the following code into a file and run it:

#python

rows = []
for rowindex in range(0,100,10):
    row = []
    for columnindex in range(0,10):
        row.append(rowindex + columnindex)
    rows.append(row)

for row in rows:
    for element in row:
        print("{:<3}".format(element), end="")
    # print with no argument just prints a newline character
    print()

print()
print("fifth row, seventh column is {}".format(rows[4][6]))

for row in rows[2:5]:
    for element in row[3:8]:
        print("{:<3}".format(element), end="")
    print()


# really try to understand it.

# now, write code that prints a 2-dimensional subsection of the array of numbers
#just print the 4th through 8th columns of the 3rd through 5th rows.

# don't use range(), use slice indexing a 