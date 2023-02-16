# grade.py
# Author Niall HOrgan

# Inputs grade and outputs award

grade = int(input("Enter your grade: "))

if (grade < 40):
    print ("Fail")
elif (39 < grade < 50):
    print ("Pass")
elif (49 < grade < 60):
    print ("Merit 2")
elif (59 < grade < 70):
    print ("Merit 1")
else:
    print ("Distinction")