
import matplotlib.pyplot as plt

# Your frequency data
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extract keys and values for plotting
keys = list(freq.keys())
values = list(freq.values())

# Create the bar chart
plt.bar(keys, values)

# Set labels and title
plt.xlabel('Keys')
plt.ylabel('Frequency')
plt.title('Histogram of Frequencies')

# Show grid for better visibility
plt.grid(axis='y')

# Display the plot
plt.show()
