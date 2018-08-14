## Day 5 Exercise 3 - Word Count
##### Objective 1 
#Write a function that takes a filename, examines the file, and 
# prints the most common word.
# Test variable
file = 'article.txt'

# open file and convert txt file to a list
def open_and_create_list(filename):
    with open(filename, 'r') as open_file:
        data = open_file.read().replace('\n', '')
        split_data = data.split(' ')
        return split_data

# return a dictionary of word-freqency pairs
def list_to_freq_dict(split_data):
    wordfreq = [split_data.count(i) for i in split_data]
    freqdict = dict(zip(split_data,wordfreq))
    freqdict_key = [(freqdict[key], key) for key in freqdict]
    return freqdict_key
    
# return most frequent word
def frequent_word(freqdict_key):
    return max(freqdict_key)

# return most frequent words in descending order
def frequent_descend(freqdict_key):
    freqdict_key.sort()
    freqdict_key.reverse()
    return freqdict_key

y = frequent_word(list_to_freq_dict(open_and_create_list(file)))
print(y)

x = frequent_descend(list_to_freq_dict(open_and_create_list(file)))
print(x)




##### Objective 2

# Write a function that takes a filename, examines the file, and 
# prints the n most common words in descending order.

##### Hint:

# Create your own simple file with test data

# This would be a good time for a data structure that has words for 
# keys instead of numbers.