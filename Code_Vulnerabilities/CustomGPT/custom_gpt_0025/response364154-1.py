
import matplotlib.pyplot as plt

# Sample frequency data
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extract keys and values
keys = list(freq.keys())
values = list(freq.values())

# Create a bar chart
plt.bar(keys, values)

# Labeling the axes
plt.xlabel('Numbers')
plt.ylabel('Frequency')

# Title of the chart
plt.title('Histogram of Frequencies')

# Show grid for better readability
plt.grid(axis='y')

# Show the bar chart
plt.show()
