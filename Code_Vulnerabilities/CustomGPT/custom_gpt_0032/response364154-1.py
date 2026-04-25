
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 7: 350, 11: 500, 20: 200, 40: 3, 41: 1, 43: 1}

# Extract keys and values from the dictionary
keys = list(freq.keys())
values = list(freq.values())

# Create the bar chart
plt.bar(keys, values)

# Label the axes
plt.xlabel('Keys')
plt.ylabel('Values')
plt.title('Bar Chart of Frequency')

# Show the plot
plt.xticks(keys)  # Show all keys on the X-axis
plt.show()
