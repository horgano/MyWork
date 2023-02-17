# guess.py
# Author Niall Horgan
#
# Input guess a number until numbreer is guessed correctly

import random
number_to_guess = random.randint(1,100)

guess = int(input("Guess the number between 1 and 100: "))

while (guess != number_to_guess):
    if (guess < number_to_guess):
        print ("Too low")
    elif (guess > number_to_guess ):
        print ("Too high")

    guess = int(input("Please guess again: "))

print (f"Yes that is correct: Eureka! {number_to_guess} was the number.")