
import matplotlib.pyplot as plt

# Your frequency data in a dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Prepare the X and Y data
x = list(freq.keys())  # Extract the keys (X-axis values)
y = list(freq.values())  # Extract the values (Y-axis values)

# Create the bar chart
plt.bar(x, y)

# Add labels and a title
plt.xlabel('Keys')
plt.ylabel('Frequency')
plt.title('Histogram of Frequency Data')

# Show the plot
plt.show()
