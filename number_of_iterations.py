# A program for plotting the number of iterations in a collatz cycle

import numpy as np
import matplotlib.pyplot as plt
import time

max_num = 20000
dim = (max_num, 2)
result = np.zeros(dim)

for n in range(1, max_num+1):
    result[n-1, 0] = n
    i = n  # used as placeholder since n is being changed in loop
    j = n
    counter = 0
    # print(result)
    while True:
        if (n % 2) == 0:
            n = int(n / 2)  # convert float to int
            if j > n:
                j = n
            elif n == j:  # a condition to check if n is stuck in a loop
                result[i-1, 1] = counter
                break
            counter += 1
        elif n == 1:
            result[i-1, 1] = counter  # enter number of iterations in array
            break  # go to next value of n
        else:
            n = int(3*n+1)  #
            counter += 1

print(result)

# plt.rcParams["figure.autolayout"] = True

x = np.array(result[:, 0])
y = np.array(result[:, 1])

plt.title("Number of iterations in 3n-1")
plt.plot(x, y, 'ro', ms=2, color='blue')

plt.show()
