
import matplotlib.pyplot as plt

# Your frequency data
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extract keys and values
keys = list(freq.keys())
values = list(freq.values())

# Create the bar chart
plt.bar(keys, values)

# Add labels and title
plt.xlabel('Numbers')
plt.ylabel('Frequency')
plt.title('Frequency Histogram')
plt.xticks(keys)  # Show all keys on the x-axis

# Show the plot
plt.show()
