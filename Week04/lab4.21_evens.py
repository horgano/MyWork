# evens.py
# Author
# 
# Prints out all the even numbers 1-100

import time

even_number = 2
number_to = 100

while even_number <= 100:
    print (f'{even_number}\n\n')
    time.sleep(1)
# https://stackoverflow.com/questions/510348/how-do-i-make-a-time-delay
    even_number += 2

