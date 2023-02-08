# div.py
# Author Niall Horgan

# Input reads 2numbers and divides the 1st one bby the 2nd one

int1 = int(input("Enter 1st number: "))
int2 = int(input("Enter 1st number: "))
answer = int1//int2
remainder = int1%int2
print (f"{int1} divided by {int2} is: {answer} with remainder: {remainder}")
