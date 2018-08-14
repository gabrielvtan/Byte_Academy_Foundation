
#
# A line read from a file contains its '\n' character
# so a print statement that ends a line with a newline
# will print an extra blank line after a line from a file
#

def one_line(filename):
    open_file = open(filename, 'r')
    line = open_file.readline()
    open_file.close()
    return line

def print_lines(filename, end="\n"):
    with open(filename, 'r') as open_file:
        for line in open_file:
            print(line, end="")

def return_lines(filename):
    output_list = []
    with open(filename, 'r') as open_file:
        for line in open_file:
            output_list.append(line)
        return output_list

# this will overwrite the file
def output_lines(filename, line_list):
    """ output_lines(filename, line_list)
            filename : name of file to write to
            line_list: a list of strings """
    with open(filename, 'a') as open_file:
        for line in line_list:
            print(line, file=open_file)
            # open_file.write("{}\n".format(line))

# add lines to the end of a file, note the 'a' parameter
def append_string(filename, string):
    with open(filename, 'a') as open_file:
        print(string, file=open_file)