first_string = "some word of different length"
second_string="zero one two three four five six seven eight nine"

# don't use default values for testing like this. I am only doing
# this in the interest of keeping the lecture moving
def word_list(string=first_string):
    return string.split()

# return a list corresponding to the length of each word in string
#
# mini exercise: construct a dictionary with each word as a key and the
# length of each word as the value
def length_list(string=second_string):
    a_list = []
    for word in string.split():
        a_list.append(len(word))
    return a_list

    # also would have worked
    return [len(word) for word in word_list(string)]

# only print lines with a given substring in them
def find_line(filename, string):
    with open(filename, 'r') as open_file:
        for line in open_file:
            if string in line:
                print(line, end="")

def words_per_line(filename):
    a_list = []
    with open(filename) as input_file:
        for line in input_file:
            words = line.split() # a list where every entry is a string
            a_list.append(len(words))
    return a_list