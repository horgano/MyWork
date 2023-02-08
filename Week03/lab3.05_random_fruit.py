# random_fruit.py
# Author Niall Horgan

import random

fruits = ('Apple','Orange','Pear','Kiwi','Grapefruit','Pineapple')

index = random.randint(0,len(fruits)-1)
fruit = fruits[index]

print (f"A random fruit is {fruit}")
    
x = random.choice(fruits)
print (f'"random.choice" generated {x}')