 # random.py
 # Author Niall Horgan
 #
 # Generate random number between 1 and 100 
 # and guess number

import random
 
number_to_guess = random.randint(1,100)

guess = int(input("Guess a number between 1 and 100: "))

while (guess != number_to_guess):
    if (guess < number_to_guess):
        print ("Too low ")
    elif (guess > number_to_guess):
        print ("Too High ")
    guess = int(input("Please guess again "))

print ("Eureka, that is the correct number.")
