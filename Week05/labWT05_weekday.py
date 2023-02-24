# weekday.py
# Author Niall Horgan

import datetime
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]

current_date = datetime.datetime.now()
today = current_date.strftime("%A")

# print (current_date.strftime("%A"))

if today in weekdays:
        print ("\nYes, unfortunately today is a weekday")
elif today in weekend:
        print ("\nIt is the weekend, yay!")
