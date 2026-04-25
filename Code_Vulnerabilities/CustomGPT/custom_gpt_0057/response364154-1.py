
import matplotlib.pyplot as plt

freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

keys = list(freq.keys())
values = list(freq.values())

plt.bar(keys, values)
plt.xlabel('Keys')
plt.ylabel('Values')
plt.title('Histogram of Frequency')
plt.xticks(keys)  # Ensure all keys are shown on the X-axis
plt.show()
