
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Prepare data for plotting
keys = list(freq.keys())
values = list(freq.values())

# Create the bar chart
plt.bar(keys, values)

# Set labels and title
plt.xlabel('Keys')
plt.ylabel('Frequency')
plt.title('Histogram of Frequencies')

# Show the grid for better readability
plt.grid(axis='y')

# Display the plot
plt.show()
