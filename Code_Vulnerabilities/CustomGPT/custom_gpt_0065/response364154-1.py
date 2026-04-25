
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Get the keys and values from the dictionary
x = list(freq.keys())
y = list(freq.values())

# Create a bar chart
plt.bar(x, y)

# Add labels and title
plt.xlabel('Keys')
plt.ylabel('Values')
plt.title('Histogram of Frequencies')

# Show the plot
plt.xticks(x)  # Show all keys on the X axis
plt.show()
