# grade.py
# Author Niall HOrgan

# Inputs grade and outputs award

grade = float(input("Enter your grade to 2 decimals: "))

if (grade < 39.5):
    print ("Fail")
elif (grade < 49.5):
    print ("Pass")
elif (grade < 59.5):
    print ("Merit 2")
elif (grade < 69.5):
    print ("Merit 1")
else:
    print ("Distinction")