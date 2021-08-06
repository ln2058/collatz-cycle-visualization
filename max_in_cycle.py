# A program for plotting the highest value reached in a collatz cycle

import numpy as np
import matplotlib.pyplot as plt

max_num = 10000
dim = (max_num, 2)
result = np.zeros(dim)

for n in range(1, max_num+1):
    result[n-1, 0] = n
    i = n  # used as placeholder since n is being changed in loop
    j = n  # used as second placeholder to calculate max value
    while n > 0:
        if (n % 2) == 0:
            n = int(n / 2)  # convert float to int

        elif n == 1:
            result[i-1, 1] = j  # enter number of iterations in array
            break  # go to next value of n
        else:
            n = 3*n+1
            if n > j:
                j = n  # set max value

x = np.array(result[:, 0])
y = np.array(result[:, 1])

plt.title("Highest number in collatz cycle")
# plot x,y set marker size and colors
plt.plot(x, y, 'ro', marker='o', ms=0.5, color='blue')

plt.ylim(0, 100000)  # scaling the y axis

plt.show()
