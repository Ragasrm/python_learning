"""
    Coding Exercise 1
Your task is to create a program that generates a random whole number. Here is how the program should behave:




As you can see, the program first asks the user to enter a whole number. Then, once the user enters a number, the program asks the user again to enter another number.

Then, the program returns a random number that falls between the two whole numbers. Here is another example:
"""

import random
first_number_user = int(input("Enter the first whole Number:"))
second_number_user = int(input("Enter the first whole Number:"))

randomNumber = random.randint(first_number_user,second_number_user)
print(randomNumber)

