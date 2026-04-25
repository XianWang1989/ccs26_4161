
import matplotlib.pyplot as plt

# Your frequency data
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Prepare the data
keys = list(freq.keys())
values = list(freq.values())

# Create the bar chart
plt.bar(keys, values)

# Add labels and title
plt.xlabel('Keys')
plt.ylabel('Values')
plt.title('Frequency Histogram')

# Show the plot
plt.xticks(keys)  # Show all keys on the x-axis
plt.show()
