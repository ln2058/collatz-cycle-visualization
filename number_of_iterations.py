# A program for plotting the number of iterations in a collatz cycle

import numpy as np
import matplotlib.pyplot as plt

max_num = 20000
dim = (max_num, 2)
result = np.zeros(dim)
counter = 0


for n in range(1, max_num+1):
    result[n-1, 0] = n
    i = n  # used as placeholder since n is being changed in loop
    while n > 0:
        if (n % 2) == 0:
            n = int(n / 2)  # convert float to int
            counter += 1
        elif n == 1:

            result[i-1, 1] = counter  # enter number of iterations in array
            counter = 0   # reset counter
            break  # go to next value of n
        else:
            n = 3*n+1
            counter += 1

plt.rcParams["figure.autolayout"] = True

x = np.array(result[:, 0])
y = np.array(result[:, 1])

plt.title("Number of iterations in collatz cycle")
plt.plot(x, y, 'ro', marker='o', ms=0.5, color='blue')

plt.show()
