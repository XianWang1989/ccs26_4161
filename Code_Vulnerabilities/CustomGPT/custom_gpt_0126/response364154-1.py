
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Separate the keys and values
keys = list(freq.keys())
values = list(freq.values())

# Create the bar chart
plt.bar(keys, values)

# Labeling the axes
plt.xlabel('Keys')
plt.ylabel('Frequency')
plt.title('Bar Chart of Frequencies')

# Show the plot
plt.xticks(keys)  # Set x-ticks to be the keys
plt.show()
