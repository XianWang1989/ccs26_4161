
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extracting the keys and values from the dictionary
keys = list(freq.keys())
values = list(freq.values())

# Creating the bar chart
plt.bar(keys, values)

# Adding labels and a title
plt.xlabel('Keys')
plt.ylabel('Values')
plt.title('Histogram of Frequency')

# Show the plot
plt.show()
