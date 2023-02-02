#hello2.py
#This takes name as input and prints 'Hello 'Name'' in 3 different styles of programming

name = input('What is your name? ')

print ('Hello ' + name + '. Nice to meet you')
print (f'Hello {name}. Nice to meet you.')
print ('Hello {}. Nice to meet you'.format(name))
        