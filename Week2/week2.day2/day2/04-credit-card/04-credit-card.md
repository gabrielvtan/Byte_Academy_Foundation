## Foundation Week 2 Day 2 Exercise 4 (Challenge) - Credit Card

#### Let's wrap the credit card processor in a class!

* Create a class, its constructor (_____init__) method should take an argument,
  number.
  
  * The class definition will have two members: number and cardtype.

  The initialization should call methods that determine if the card
  is valid, and the card type. If the card is not valid, set cardtype equal to
  None. Otherwise, set it equal to "Visa", "Mastercard", or "AMEX"

  * * write your validation logic as a method that you call with
  self.validate() in the __init__(number) method.

#### Challenge: `__str__`

  * The special `__str__` method of a class determines how the class outputs
  when printed. Create this method for your credit card class and have it
  either display as
  ```
  'Invalid Card'

  or

  'Visa: 1111 1111 1111 1111'
