import numpy as np
import matplotlib.pyplot as plt

max_num = 10000
result = np.zeros((max_num, 3))

for n in range(1, max_num+1):
    # State rules for odd and even

    # Have variables to store data
    tracker = [n]
    i = n
    while True:
        if (n % 2) == 0:
            n = int((3*n)-1)
            if n in tracker:
                result[i-1, 0] = tracker[0]
                result[i-1, 1] = len(tracker)
                tracker.sort()
                result[i-1, 2] = tracker[-1]
                break
            else:
                tracker.append(n)
        else:
            n = int((n/2)+0.5)
            if n in tracker:
                result[i-1, 0] = tracker[0]
                result[i-1, 1] = len(tracker)
                tracker.sort()
                result[i-1, 2] = tracker[-1]
                break
            else:
                tracker.append(n)

# print(result)

num = np.array(result[:, 0])
iterations = np.array(result[:, 1])
max_num = np.array(result[:, 2])

f = plt.figure(1)
plt.title("Number of iterations")
plt.plot(num, iterations, 'ro', ms=2, color='blue')
f.show()

g = plt.figure(2)
plt.title("Max value reached in cycle")
plt.plot(num, max_num, 'ro', ms=2, color='blue')
g.show()

plt.show()
