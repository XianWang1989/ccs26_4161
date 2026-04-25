
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Getting the keys and values from the dictionary
keys = list(freq.keys())
values = list(freq.values())

# Creating the bar chart
plt.bar(keys, values)

# Adding titles and labels
plt.title('Frequency Histogram')
plt.xlabel('Keys')
plt.ylabel('Frequency')

# Displaying the plot
plt.xticks(keys) # To ensure all keys are shown on the x-axis
plt.show()
