from pprint import pprint # little utility that is useful for testing with dictionaries

dictionary = {
    "key1" : 0,
    "key2" : 1,
    "key3" : [1, 2, 3, 4, 5],
    10 : "ten",
    20 : "twenty",
    "a sub dictionary" : {
        "a" : "A!",
        "b" : "B!",
        "a list" : [True, False]
    }
}
 
def dictionary_example():

    print("output:")
    print(dictionary)
    print()
    print("string key:")
    print(dictionary["key2"])
    print()
    print("numeric key")
    print(dictionary[10])
    print()
    print("nested structures with multiple indices")
    print(dictionary["key3"])
    print(dictionary["key3"][2])
    print(dictionary["a sub dictionary"])
    print(dictionary["a sub dictionary"]["a"])
    print(dictionary["a sub dictionary"]["a list"][1])
    print()
    print("pprint")
    print()
    pprint(dictionary)
    print()
    print("change a value")
    dictionary["key2"] = "New value"
    print(dictionary["key2"])
    print()
    print("new key")
    dictionary["new value"] = "NEW"
    print(dictionary["new value"])
    print()
    print("remove key")
    del(dictionary["new value"])
    print()
    print("what if you're not sure if a key exists?")
    print(dictionary.get("key2", "default"))
    print(dictionary.get("not a key", "default"))

ordered = {
    1 : 'one',
    4 : 'four',
    0 : 'zero',
    2 : 'two',
    'list' : [1, 2, 3, 4],
    'z' : 'Z',
    'b' : None,
    'c' : 'C',
    'd' : 'D',
    'a' : 'A'
}

# DON'T RELY ON THE KEYS BEING IN A CERTAIN ORDER!
def dictionary_loop(a_dictionary=ordered):
    for key in a_dictionary:
        print(a_dictionary[key])
        # Don't add new elements in a loop:
        # a_dictionary["new key"] = False

def modify(a_dictionary=ordered):
    a_dictionary['modification'] = True

# like a list, a dictionary is a mutable type. 
def copy_and_modify(a_dictionary=ordered):
    new_dic = dict(a_dictionary)
    for key in new_dic:
        new_dic[key] = "element: {}".format(new_dic[key])
    return new_dic