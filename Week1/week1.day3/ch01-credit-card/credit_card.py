## Day 3 Challenge 02 - Credit Card Validator

#### A real-world application
# You know now enough material to execute a useful-real world algorithm: credit card validation.
#### The assignment
# We will be using the [Luhn Algorithm](http://en.wikipedia.org/wiki/Luhn_algorithm), also known as "modulus 10", we will be determining the validity of a given credit card number.
# Prompt the user for a credit card number.
# define number and card_number_stripped
card_number = input("Give me credit card number: ")
numbers = ('1','2','3','4','5','6','7','8','9','0')
card_number_stripped = []
for x in card_number:
    if x in numbers:
        card_number_stripped.append(x)
card_number_stripped = ''.join(card_number_stripped)
card_number_stripped_list = list(map(int,card_number_stripped))
card_number_stripped_list_reverse = card_number_stripped_list[::-1]

#### The Luhn Algorithm
# multiply the digits in odd positions by 2, if product >10, then add the digits of the product
def Luhn_Algo(card_number_stripped_list_reverse):
    for index in range(1,len(card_number_stripped_list_reverse),2):
        if card_number_stripped_list_reverse[index] < 5:
            card_number_stripped_list_reverse[index] = card_number_stripped_list_reverse[index] * 2
        else:
            card_number_stripped_list_reverse[index] = ((card_number_stripped_list_reverse[index] * 2 // 10)) +((card_number_stripped_list_reverse[index] * 2 % 10))
    checksum = sum(card_number_stripped_list_reverse)
    return checksum

def Card_Validation(checksum):
#The check digit is the amount that you would need to add to get a multiple of 10
    if checksum % 10 == 0:
        print('The number is valid')
        if int(card_number_stripped[0]) == 4:
            print('Visa')
        elif 51 <= int(card_number_stripped[:2]) <= 55:
            print('Mastercard')
        elif int(card_number_stripped[:2]) == 34 or int(card_number_stripped[:2]) == 37:
            print('Amex')
        elif int(card_number_stripped[:5]) == 6011:
            print('Discover')
        else:
            print('The card is not valid')
        

Card_Validation(Luhn_Algo(card_number_stripped_list_reverse))


# Determine if the card is valid and what type of card it is.

# * Here is a test value: 347650202246884. It is a valid Amex.

### The algorithm

#### Card type and length
# Visa must start with 4
# Mastercard must start with 51, 52, 53, 54 or 55
# AMEX must start with 34 or 37
# Discover must start with 6011
# Visa, MC and Discover have 16 digits
# AMEX has 15 digits
# * You already know a card is invalid if it is the wrong length or isn't any type. You can go ahead and say so and use quit() to exit the program 
# without the rest of the test.


# For example:
# 4 4 8 5 0 4 0 9 9 3 2 8 7 6 1 6`
# becomes
#`8 4 16 5 0 4 0 9 18 3 4 8 14 6 2 6`



# Now, sum all the individual digits together. That is to say, split any numbers with two digits into their individual digits and add them. Like so:

#`8 + 4 + 1 + 6 + 5 + 0 + 4 + 0 + 9 + 1 + 8 + 3 + 4 + 8 + 1 + 4 + 6 + 2 + 6`

# Now take the sum of those numbers and modulo 10.

# 80 % 10

# If the result is 0, the credit card number is valid.

### Business Logic

# "Business Logic" are the requirements and specifications imposed on your code by its real-world application. 
# It is often the cause of code that is messier than software developers would like. This
# is where writing good comments that describe what is going on really pay off! A stranger will have to
# read your code and maintain it someday, and code you wrote 6 months ago and haven't looked at since might
# as well have been written by a stranger!
