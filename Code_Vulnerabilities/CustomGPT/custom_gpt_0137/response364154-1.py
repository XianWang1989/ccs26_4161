
import matplotlib.pyplot as plt

# Your data in a dictionary
freq = {1: 1000, 2: 980, 4: 560, 5: 450, 6: 300, 7: 150, 8: 100, 40: 3, 41: 1, 43: 1}

# Extract keys and values from the dictionary
x = list(freq.keys())  # X-axis values (the keys)
y = list(freq.values())  # Y-axis values (the corresponding frequencies)

# Create a bar chart
plt.bar(x, y)

# Set titles and labels
plt.title('Histogram of Frequencies')
plt.xlabel('Keys')
plt.ylabel('Frequencies')

# Show the grid for better readability
plt.grid(axis='y')

# Display the plot
plt.show()
