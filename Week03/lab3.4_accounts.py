# accounts.py
# Author Niall Horgan
# Firtsly read in a 10 digit number and output first 6 numbers 
# replaced with X's and final 4 numbers as is.
# Secondly read in any length account number 
# and replace all but final 4 digits with X's

account_number = str(input("Enter your 10 digit account number: "))
final4 = account_number[-4:]

print (f'"XXXXXX{final4}"')