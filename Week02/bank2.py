#Read 2 numbers(integers), add both and return answer in EURO form

#Author: Niall Horgan

#
num1 = int(input("Please enter number1 in cents: ",))
print ('For number 1 you entered: ', (num1))

num2 = int(input('Please enter number2 in cents: '))
print ('For number 2 you entered: ', (num2))

sum = num1 + num2

print ('The sum of your 2 numbers in EURO format is: €{}'.format(sum/100))
