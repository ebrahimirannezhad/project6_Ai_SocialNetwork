import numpy as np
import matplotlib.pyplot as plt

def simulate_rioting(thresholds):
    n = len(thresholds)
    state = [0] * n
    for i in range(n):
        if state[i] == 0:
            if sum(state[j] >= thresholds[j] for j in range(n)) >= thresholds[i]:
                state[i] = 1
    return sum(state)

# Define the vector of thresholds
T = [1, 1, 1, 1, 1, 4, 1, 0, 4, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 4, 0, 1, 4, 0, 1, 1, 1,
     4, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 4, 1, 1, 4, 1, 4, 0, 1, 0, 1, 1,
     1, 0, 4, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 4, 0, 4, 0, 0, 1, 1, 1,
     4, 0, 4, 0]

# Simulate the rioting behavior 1000 times and store the results in a histogram
results = [simulate_rioting(T) for _ in range(1000)]
n = len(T)
hist, bins = np.histogram(results, bins=np.arange(n+2))

# Plot the histogram
plt.bar(range(n+1), hist, align='center')
plt.xticks(range(n+1))
plt.xlabel('Number of individuals with threshold k')
plt.ylabel('Number of simulations with that result')
plt.show()