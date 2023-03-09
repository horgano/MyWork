# bank.py

#Read 2 numbers(integers), add both and return answer in EURO format

#Author: Niall Horgan

num1 = int(input('Enter amount1 (in cents): '))
num2 = int(input('Enter amount2 (in cents): '))

sum = num1 + num2

print (f'The sum of these 2 numbers in EUROs is: €{sum/100}')
print (f'The sum of these 2 numbers in EUROs is: €{sum/100}')
print ('The sum of these 2 numbers in EUROs is: €{}'.format(sum/100))
