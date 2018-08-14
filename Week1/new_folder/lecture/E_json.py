# json is a file format for storing dictionaries

import json

# json files are a lot like python dictionaries.
# the datatypes they can hold as values are strings, numeric types, booleans,
# None, lists, and sub-dictionaries. 
# 
# boolean values are lowercased. None is null in json

# a json file starts with an open curly brace and keys can only be strings

# Default filenames can sometimes be OK. If a file is acting like a 'database' and
# there's a standard name
def load_dictionary(filename='example.json'):
    with open(filename, 'r') as jsonfile:
        return json.load(jsonfile)

example_dict = {
    "a" : "first value",
    "b" : ["list", "value"],
    "c" : {
        1: None,
        2: 0,
        3: 1
    }
}

# Again, don't use test data as default values in real work. This is
# just for lecture
def write_json(filename, dictionary=example_dict):
    with open(filename, 'w') as jsonfile:
        json.dump(dictionary, jsonfile)

def dic_to_json_string(dictionary=example_dict):
    return json.dumps(dictionary)
