## Day 4 Exercise 3 - Variable Caps

# Write a function that takes a word as its argument
# If the word is 3 letters or shorter, return the original input. If the word is 4 letters or longer, return the word in ALLCAPS.
# So 'the' would stay 'the' but 'homework' would become 'HOMEWORK'

def capitals(x):
    if len(x) <= 3:
        return x
    else:
        return x.upper()

# Now write a function that takes a sentence in its argument and returns a string where the first function is applied to every word.
# Hint: str.split
# For example:
# * Now is the time for all good men to come to the aid of their country
# * Now is the TIME for all GOOD men to COME to the aid of THEIR COUNTR

def sentence(x):
    x_split = x.split(" ")
    for i in x_split:
        if len(i) <= 3:
            print (i, end =" ")
        else:
            print (i.upper(), end =" ")
    print('\n')

# Now prompt the user for an input and print the processed string.
y = input("give me a word: ")
y = sentence(y)


