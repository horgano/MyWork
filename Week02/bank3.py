#Read 2 numbers(integers), add both and return answer in EURO format

#Author: Niall Horgan

num1 = int(input('Enter amount1 (in cents): '))
num2 = int(input('Enter amount2 (in cents): '))

newNum = (float(num1 + num2))/100

print (f'The sum total in EUROs is: €{newNum}')
