import numpy as np
import matplotlib.pyplot as plt


def input_function():
    # Enter values with appropriate operations in terms of n
    rule_even = input("Enter rule for even integer: ")
    rule_odd = input("Enter rule for odd integer: ")
    min_num = int(input("Enter minimum start value: "))
    max_num = int(input("Enter maximum start value: "))
    return rule_even, rule_odd, min_num, max_num


def collatz_master():
    rule_even, rule_odd, min_num, max_num = input_function()
    result = np.zeros((abs(max_num)+abs(min_num)+1, 3))
    i = -1
    for n in range(min_num, max_num+1):
        # State rules for odd and even

        # Have variables to store data
        tracker = [n]
        i += 1
        while True:
            if (n % 2) == 0:    # even
                n = int(eval(rule_even))
                if n in tracker:
                    result[i, 0] = tracker[0]   # counts as initial number
                    # counts as number of iterations
                    result[i, 1] = len(tracker)
                    tracker.sort()
                    min = tracker[0]
                    max = tracker[-1]
                    if abs(min) > abs(max):  # check to see if max is negative number of positive
                        result[i, 2] = min
                    elif abs(min) < abs(max):
                        result[i, 2] = max
                    elif abs(min) == abs(max):
                        result[i, 2] = max
                    break
                else:
                    tracker.append(n)
            else:     # off
                n = int(eval(rule_odd))
                if n in tracker:
                    result[i, 0] = tracker[0]
                    result[i, 1] = len(tracker)
                    tracker.sort()
                    min = tracker[0]
                    max = tracker[-1]
                    if abs(min) > abs(max):  # check to see if max is negative number of positive
                        result[i, 2] = min
                    elif abs(min) < abs(max):
                        result[i, 2] = max
                    elif abs(min) == abs(max):
                        result[i, 2] = max
                    break
                else:
                    tracker.append(n)

    # print(result) # if you want in array form

    # Plotting data on graphs
    num = np.array(result[:, 0])
    iterations = np.array(result[:, 1])
    max_num = np.array(result[:, 2])


    f = plt.figure(1)
    plt.title("Number of iterations")
    plt.plot(num, iterations, 'ro', ms=0.5, color='blue')
    f.show()

    g = plt.figure(2)
    plt.title("Max value reached in cycle")
    plt.plot(num, max_num, 'ro', ms=0.5, color='blue')

    max_num.sort()
    min_bound = float((max_num[0])/300)
    max_bound = float((max_num[-1])/300)

    plt.ylim(min_bound, max_bound)  # scaling the y axis
    g.show()

    plt.show()


collatz_master()
