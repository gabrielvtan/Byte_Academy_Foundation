## Foundation Week 2 Day 2 Exercise 4 (Challenge) - Credit Card

#### Let's wrap the credit card processor in a class!

# Create a class, its constructor (_____init__) method should take an argument,
# number.
  
# The class definition will have two members: number and cardtype.

#The initialization should call methods that determine if the card
#is valid, and the card type. If the card is not valid, set cardtype equal to
#None. Otherwise, set it equal to "Visa", "Mastercard", or "AMEX"

# * write your validation logic as a method that you call with
#self.validate() in the __init__(number) method.

#### Challenge: `__str__`

# The special `__str__` method of a class determines how the class outputs
#when printed. Create this method for your credit card class and have it
#either display as
```
#'Invalid Card'

#or

#'Visa: 1111 1111 1111 1111'
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
