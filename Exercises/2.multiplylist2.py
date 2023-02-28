# multiply all numbers in a list
# https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-2.php

def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
print(multiply_list([1,2,-8]))