# root_newton.py
# Author Niall Horgan
# Get the square root of a number



num = float(input("Please enter a positive number: "))
    
guess = num / 2.0
while abs(num - guess ** 2) > .0001:
    guess = (guess + num / guess) / 2.0
print (guess)
    

