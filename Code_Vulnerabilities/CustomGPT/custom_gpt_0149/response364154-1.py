
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extract keys and values from the dictionary
keys = freq.keys()
values = freq.values()

# Create a bar chart
plt.bar(keys, values)

# Add labels and title
plt.xlabel('Keys')
plt.ylabel('Frequency')
plt.title('Frequency Histogram')

# Show the plot
plt.xticks(keys)  # Ensure all keys are shown on the X-axis
plt.show()
