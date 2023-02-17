# averages.py
# Author Niall HOrgan   
#
# Input a number of numbers until input '0' to quit
# and return the average of the numbers

numbers = []

number = int(input("Enter a number (or 0 to quit): "))
    
while (number != 0):
    numbers.append(number)
    number = int(input("Enter another: "))

for number in numbers:
    print(number)

average = float(sum(numbers)) / len (numbers)
print(f"The average of your numbers is: {average}")
