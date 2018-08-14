## Day 5 Exercise 4 json & dictionary
# In this folder is a json file for a snapshot of Tesla's 
# market information.
import json
from pprint import pprint

file = 'test.json'

# Open the file and load it into a dictionary
# Print a list with every key and its value (use a loop)
def load_dictionary(file):
    with open(file, 'r') as jsonfile:
        dictionary = json.load(jsonfile)
        dictionary_list = []
        for key, value in dictionary.items():
            dictionary_list.append([key, value])
        return dictionary_list

# Create a new dictionary with just the Name, Symbol, 
# LastPrice and Volume keys.
def new_dictionary(file):
    with open(file, 'r') as jsonfile:
        dictionary = json.load(jsonfile)
        keys = ['Name', 'Symbol', 'LastPrice', 'Volume']
        dictionary_new = {x:dictionary[x] for x in keys}
        return dictionary_new


# Write that dictionary to a json file with the name 'tsla_summary.json'
def write_new_dict(filename, dictionary):
    with open(filename, 'w') as jsonfile:
        json.dump(dictionary, jsonfile)


write_new_dict('tsla_summary.json', new_dictionary(file))


#print(write_new_dict(dictionary_new,'tsla_summary.json'))
        
