#Read in a name and age and out put sentence
#I like to do it in 3 formats

name = input('Please enter your name: ')
age = int(input('Please enter your age: '))

print (f'Hello {name}, your age is {age}')
print ('Hello ' + name + ', your age is ' + str(age))
print ('Hello {}, your age is {}'.format(name,age))

#1 format with tab

print ('Hello {},\t your age is {}'.format(name,age))

num = 21 - 4
print (num)

