# random_generator.py
# Niall Horgan
# program that prints out a random number between 1 and 10

import random

# number = random.randint(1,10)
# print (f"A random number between 1 and 10 is: {number}")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

randomnumber = random.randint(num1,num2)
print (f'A random number between {num1} and {num2} is: {randomnumber}')
