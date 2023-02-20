# collatz.py
#
# Input a positive integer
# While not equal to 1 (when == 1 end calc)
# If int is even -> divide by 2
# If int is odd  -> multiply by 3 and add 1
# Output successive calcs until program ends

x = int(input("Enter a positive integer: "))

collatz = []

while (x != 1):
    if ((x % 2) == 0):
        x = (x / 2)
        collatz.append (int(x))
    elif ((x % 2) ==1):
        x = ((x * 3) + 1)
        collatz.append (int(x))

print (collatz)

16: