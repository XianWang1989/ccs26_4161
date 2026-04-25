
import matplotlib.pyplot as plt

# Sample frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extract keys and values
keys = list(freq.keys())
values = list(freq.values())

# Create the bar chart
plt.bar(keys, values)

# Labeling the axes
plt.xlabel('Data Points')
plt.ylabel('Frequency')
plt.title('Histogram of Frequencies')

# Show the plot
plt.xticks(keys)  # Ensure all keys are shown on x-axis
plt.show()
