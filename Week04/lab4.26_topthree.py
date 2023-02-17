# topthree.pt
# Author Niall Horgan
#
# Generates 10 random numbers, prints them out and then rints top three
#
# Numbers to be stored in list to be manipulated

import random

range_from = 0
range_to = 100
how_many = 10
top_how_many = 4

numbers = []

for i in range(0,how_many):
    numbers.append(random.randint(range_from, range_to))
print (f'{how_many} random numbers: \t {numbers}')

top_ones = numbers.copy()

top_ones.sort(reverse=True)
shortlist = top_ones[0:top_how_many]
# print (top_ones)
print (f"'The top {top_how_many} numbers are:\t\t {shortlist}")

