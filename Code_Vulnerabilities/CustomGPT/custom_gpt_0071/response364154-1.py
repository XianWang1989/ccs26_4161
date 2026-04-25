
import matplotlib.pyplot as plt

# Your frequency data
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extract keys and values for plotting
keys = list(freq.keys())
values = list(freq.values())

# Create the bar chart
plt.bar(keys, values)

# Label the axes
plt.xlabel('Keys')
plt.ylabel('Frequency')

# Add a title
plt.title('Bar Chart of Frequencies')

# Show the plot
plt.xticks(keys)  # Ensure all keys are shown on the X-axis
plt.show()
