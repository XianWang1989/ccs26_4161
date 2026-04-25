
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extract keys and values from the dictionary
keys = list(freq.keys())
values = list(freq.values())

# Create the bar chart
plt.bar(keys, values)

# Add labels and title
plt.xlabel('Keys')
plt.ylabel('Values')
plt.title('Histogram of Frequencies')

# Show gridlines for better readability
plt.grid(axis='y')

# Display the plot
plt.show()
