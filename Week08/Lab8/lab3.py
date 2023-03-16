# historam of salaries

import numpy as np
import matplotlib.pyplot as plt

min_salary = 20000
max_salary = 80000
number_of_salarys = 10

np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, number_of_salarys)
ages =np.random.randint(18, 68, number_of_salarys)

salaries2 = salaries + 5000
salaries3 = salaries * 1.05

# To change salaries3 to an integer
salaries4 = salaries3.astype(int)

print (salaries)


# print (salaries2)
# print (salaries4)

plt.hist(salaries)
plt.show()