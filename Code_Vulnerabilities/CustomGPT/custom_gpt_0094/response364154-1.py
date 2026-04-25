
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extract keys and values
keys = list(freq.keys())
values = list(freq.values())

# Create a bar chart
plt.bar(keys, values)

# Labeling the axes
plt.xlabel('Keys')
plt.ylabel('Values')
plt.title('Histogram of Frequency Data')

# Show the plot
plt.xticks(keys)  # Ensure all keys are shown on the x-axis
plt.show()
