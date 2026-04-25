
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extract keys and values from the dictionary
keys = list(freq.keys())
values = list(freq.values())

# Create a bar chart
plt.bar(keys, values)

# Label the axes
plt.xlabel('Keys')
plt.ylabel('Values')

# Set the title
plt.title('Bar Chart of Frequency')

# Show the plot
plt.xticks(keys)  # Ensure all keys are displayed on the X-axis
plt.show()
