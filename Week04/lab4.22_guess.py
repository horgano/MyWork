# guess.py
# Author Niall Horgan
#
# Input guess a number until numbreer is guessed correctly

number_to_guess = 15

guess = int(input("Guess the number between 1 and 20: "))

while (guess != number_to_guess):
    print ("Wrong!")
    guess = int(input("Please guess again: "))

print ("Yes that is correct: Eureka")