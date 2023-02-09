# convert.py
# Author Niall Horgan   

# Reads in a negative or positive number
# in dollars and cents and gives the absolute
# number in cents

import math

dollarsandcents = float(input("Enter your figure of dollars and cents: "))
cents = (dollarsandcents * 100)
centceiling = int(math.ceil(cents))     # https://www.w3schools.com/python/module_math.asp
#absolute = abs(centceiling)            # https://kodify.net/python/math/absolute-value/

absolute  = int(math.fabs(centceiling)) # https://kodify.net/python/math/absolute-value/

#print (absolute)
print (f"The absolute value in cents for the amount you entered is: {absolute}")
