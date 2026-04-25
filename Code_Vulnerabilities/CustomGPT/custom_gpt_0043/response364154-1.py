
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {
    1: 1000, 2: 980, 4: 560, 8: 250, 16: 100,
    20: 75, 25: 50, 30: 20, 35: 10, 40: 3, 41: 1, 43: 1
}

# Extract keys and values from the dictionary
keys = list(freq.keys())
values = list(freq.values())

# Create a bar chart
plt.bar(keys, values)

# Labeling the axes
plt.xlabel('Keys')
plt.ylabel('Values')

# Adding a title
plt.title('Histogram of Frequency Data')

# Show the plot
plt.show()
