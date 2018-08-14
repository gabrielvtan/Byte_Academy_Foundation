
# print(commas("abcdefghijklmnopqrstuvwxyz")) # it is an error to call a function before it is defined."

def commas(string):
    # you can call a function that is defined later from within a function though
    # by the time you actually use this function, the later one will be defined
    str_list = chop_up(string)
    return ", ".join(str_list)



def chop_up(string):
    return [character for character in string]


if __name__ == "__main__":
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    print(commas(alphabet)) # it is an error to call a function before it is defined."
    #
    # by putting the code in this if block, we can import the file as a module to test it
    # 
    # in the interactive environment try:
    #
    # import 01-file-structure
    # 01-file-structure.chop_up("test")