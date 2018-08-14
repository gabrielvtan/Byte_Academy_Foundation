## Interactive testing

* Now that you understand functions, you can test your code as you write it in a more efficient way.

* Make sure your filename is a legal python identifier: it starts with a letter (first character can't be a number, and it contains no spaces or dashes) so 01-homework1.py would not work but homework_01.py would.

* Navigate on the command line with cd to get into the directory your work is in. Use ls to confirm that the file is there.

* Enter python interactive mode

* Import your filename *without* the '.py' So in the above statement, you would say ```import homework_01```

* Call your functions with test input

* Make changes to your file, save the file, and then use 'reload' from the imp library to work with the new changes

* * ```from imp import reload```

* * reload(homework_01)

* This is how I work and I find it much easier than putting print statements everywhere.

* Bonus suggestion: ```from pprint import pprint``` pprint is a useful alternative to print for printing out large datastructures like 2 dimensional lists and dictionaries.