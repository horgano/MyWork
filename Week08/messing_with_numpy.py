# messing_with_numpy.py
# Author Niall Horgan

import numpy as np

list_of_numbers = [1,2,3,4,5]
print (list_of_numbers)

numbers = np.array([1,2,3,4,5])
print (numbers)
numbers = numbers + 3
print (numbers)

rando = np.random.randint(0,100,30)
print (rando)

otherrando = np.random.randint(10,size=2)
print (otherrando)

normrando = np.random.normal(loc=50, scale=20, size=2)
print (normrando)