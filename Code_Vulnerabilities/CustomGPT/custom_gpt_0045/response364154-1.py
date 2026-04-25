
import matplotlib.pyplot as plt

# Your frequency data
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extract keys and values from the dictionary
keys = list(freq.keys())
values = list(freq.values())

# Create the bar chart
plt.bar(keys, values, color='blue')

# Label the axes
plt.xlabel('Keys')
plt.ylabel('Values')

# Add a title
plt.title('Histogram from Dictionary Data')

# Show the plot
plt.xticks(keys)  # Ensure all keys are shown on the x-axis
plt.show()
