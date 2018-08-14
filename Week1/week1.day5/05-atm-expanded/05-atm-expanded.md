## Day 5 Challenge - ATM Expanded

#### Time to expand the ATM

* Your ATM should keep a record of accounts. You should design a file format that stores a card number (pretend any valid card is a debit card) a PIN and a balance.

* When the program starts, ask the user for their card number and then their PIN, compare that to the stored card number and PIN. If it matches a stored pair, take them to the main menu.

* The main menu has "Check Balance" "Deposit Money" "Withdraw Money" and "Change PIN" and "Done" options.

* * Implement each one.

* When the user selects "Done" save any changes to the data.

#### New Accounts

* At first, manually put a card number, PIN, and balance into the data

* Once you have things working, implement the ability to create a new account.

* If the user inputs a valid (reuse your old code!) card number, prompt them for a PIN and an initial deposit.

* Save the new user information.

#### Hints

* You'll probably have to overwrite the whole datafile every time you save. Make sure you're loading *all* the data, even if you're only using one account.

* Can you think of a way to not have to do this, using append?

#### Open Ended

* What other features could you have? Maybe a checking and savings account tied to the card and the ability to transfer money between them?