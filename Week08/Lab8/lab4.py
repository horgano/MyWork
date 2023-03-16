# ages with same number of random salaries

import numpy as np
import matplotlib.pyplot as plt

min_salary = 20000
max_salary = 80000
number_of_salarys = 10

np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, number_of_salarys)
ages =np.random.randint(18, 68, number_of_salarys)

print (salaries)
print (ages)

plt.scatter(salaries, ages, label = "ages", color = "blue")
# plt.show()

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

#plt.plot(xpoints, ypoints)
plt.plot(xpoints, ypoints, label = "xsquared", color = "red")

plt.title("random plot")
plt.xlabel("Salaries")
plt.ylabel("age")
plt.legend()
plt.show()