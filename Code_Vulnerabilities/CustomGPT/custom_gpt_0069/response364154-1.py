
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extract keys and values
keys = list(freq.keys())
values = list(freq.values())

# Create the bar chart
plt.bar(keys, values)

# Adding labels
plt.xlabel('Keys')
plt.ylabel('Frequency')
plt.title('Histogram of Frequency')

# Show the plot
plt.xticks(keys)  # Show all keys on the X-axis for clarity
plt.show()
