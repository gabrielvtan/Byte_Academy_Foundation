## Day 2 Exercise 6b - Disemvowel

# There was an old forum online where the moderators had a policy of 'disemvoweling' trolling posts. 
# This means modifying the text of the post to not include any vowels.

vowels = "aeiouAEIOU"
string = input("Give me a string: ")
new_string = []

for x in string:
    if x not in vowels:
        new_string.append(x)

new_string = ''.join(new_string)
print(new_string)


# Input a string and then print it out again with only the  non-vowel strings.

# This will involve a for loop and an if statement using in.