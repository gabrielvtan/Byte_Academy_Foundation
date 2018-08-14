
# print(commas("abcdefghijklmnopqrstuvwxyz")) # it is an error to call a function before it is defined."

def commas(string):
    str_list = chop_up(string) # you can call a function earlier than its definition if it doesn't
    return ", ".join(str_list) # automatically execute when the program first runs.

def chop_up(string):
    return [character for character in string]

def whoami():
    print(__name__)

if __name__ == "__main__":
    print(commas("abcdefghijklmnopqrstuvwxyz"))
    whoami()