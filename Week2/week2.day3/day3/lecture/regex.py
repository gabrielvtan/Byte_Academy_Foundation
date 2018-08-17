import re

def simple_expressions():
    print("\n\n\n\n\n")
    string = "Carter Adams"

    result = re.search("Carter", string)
    print("\nsuccessful match:" ,result)

    result = re.search("Kenso", string)
    print("\nfailed match:", result)

    # print to test if the *whole* string is a match:
    result = re.fullmatch("Carter", string)
    print("\nfullmatch test: ", result)

    # so to test if a string contains a match
    if re.match("Carter", string):
        print("Test with an if block")

def characters():
    print("\n\n\n\n\n")

    string1 = "Hi there"
    string2 = "Hi There"
    string3 = "Hi +here"
    print("\n match any character with .")
    print(re.search("Hi .here", string1))
    print(re.search("Hi .here", string2))
    print(re.search("Hi .here", string3))

    string = "Byte Academy"
    result = re.search("[ABC]yte", string)
    print("\n: match with character set: ", result)
    
    result = re.search("Academ[v-z]", string)
    print("\n: match with character range: ", result)
    print("can have multiple ranges & characters like [A-Za-z_.\-]")
    print("would match any letter, an underscore, a dot or a dash.")
    print("inside a character class, many special characters lose")
    print("their meaning, like the dot")

    result = re.search("[^WXYZ]cademy", string)
    print("\n: match with negated character set: ", result)

    string = "$900"

    result = re.search("[0-9][0-9][0-9]", string)
    print("\n: match a digit: ", result)

    result = re.search("$900", string)
    print("\n: problem with special character $: ", result)

    result = re.search("[$]900", string)
    print("\n: most special charaters are normal in [] blocks:", result)
    print("""but in [] blocks you need to escape \] \- and \^""")

def repetition():
    print("\n\n\n\n\n")
    string = "Hellooooooooo there"
    result = re.search("Hello+ there", string)
    print("\n: + matches 1 or more occurrances of a character", result)
    
    string = "Now is the time for all good men to come to the aid of their country."
    result = re.search("Now.*country\.", string)
    print("\n: * matches 0 or more occurances of a character. It is commonly used\n")
    print("with '.' to match any amount of space between other parts of the expression\n")
    print(result)

    string1 = "-567"
    string2 = "89087"
    result1 = re.search("-?\d+", string1)
    result2 = re.search("-?\d+", string2)
    print("\n ? matches 0 or 1 occurances of a character.")
    print(result1, result2)

    string = "Now is the time for all good men to come to the aid of their country."
    result = re.search(".*is.*good.*aid.*their.*", string)
    print("\n: using .* to check for words occurring in an order.", result)

    string = "My phone number is 212-555-1234"
    # there are shorthands for some character sets. \d is a digit.
    # \s is whitespace, \w is 'word' characters letters an accents
    result = re.search("\d{3}-\d{3}-\d{4}", string)
    print("\n: specifying specific numbers of repetitions: ", result)

def anchor():
    print("\n\n\n\n\n")
    string = "Carter Adams"
    result = re.search("^Carter", string)
    result2 = re.search("^Adams", string)
    print("\n ^ matches the beginning of a string", result)
    print(result2)

    result = re.search("Adams$", string)
    result2 = re.search("Carter$", string)
    print("\n $ matches the end of a string", result)
    print(result2)

def groups():
    print("\n\n\n\n\n")
    # groups create sub regular expressions
    string = "Hah hah hah hah hah, I win"
    result = re.search("([Hh]ah)+.*I win$", string)
    print("\nPut min-regexes in regular expressions with (). You can use")
    print("repetition tests with them. ", result)

    string1 = "Carter Adams is the instructor"
    string2 = "Carter Smith is the instructor"
    result = re.search("Carter (Adams )?is the instructor", string1)
    result2 = re.search("Carter (Adams )?is the instructor", string2)
    print("\nThis has a lot of uses.")
    print(result, result2)

    string = "One two three four five "
    result = re.search("(\w+) (\w+) (\w+) (\w+)", string)
    print("\nUse the group & the groups method of the result object to")
    print("capture matching sub-strings")
    print(result.groups())
    result2 = re.search("(\w+ )*", string)
    print(result2.groups())

    string1 = "Joe Frank: 212-345-6789"
    string2 = "Bill: 706-555-9876"
    string3 = "Sarah: 917-555-5820"

    def name_number(string):
        expression = "^(.+): (\d{3})-(\d{3})-(\d{4})"
        match = re.search(expression, string)
        if match is None:
            return None
        groups = match.groups()
        if len(groups) != 4:
            return None
        else:
            return {
                "name" : groups[0],
                "area code" : groups[1],
                "number" : "{}-{}".format(groups[2], groups[3])
            }

    print("\n example real use:")
    print(name_number(string1))
    print(name_number(string2))

def findall():
    string = "5000 is a big number, 3 isn't very big, 0 isn't anything, and 100 is kind of in the middle."
    matches = re.findall("\d+", string)
    print("\n Use findall to find every matching substring if a line might contain more than one.")
    print(matches)

groups()