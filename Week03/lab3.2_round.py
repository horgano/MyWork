# round.py

# Author Niall Horgan

# Take in a floating number and round to the nearest integer

number_to_round = float(input("Enter a floating number: "))
rounded_number = round(number_to_round - 0.00001)
print(f'{number_to_round} rounded is: {rounded_number}')