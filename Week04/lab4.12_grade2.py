# grade.py
# Author Niall HOrgan

# Inputs grade and outputs award

grade = int(input("Enter your grade: "))

if (grade < 40):
    print ("Fail")
elif (grade < 50):
    print ("Pass")
elif (grade < 60):
    print ("Merit 2")
elif (grade < 70):
    print ("Merit 1")
else:
    print ("Distinction")