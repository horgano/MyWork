#Read 2 numbers(integers), add both and return answer in EURO form

#Author: Niall Horgan

num1 = int(input("Enter amount1 (in cents): "))
num2 = int(input('Enter amount2 (in cents): '))

sum = num1 + num2

print ('The sum of your 2 numbers in EUROs is: €{}'.format(sum/100))
