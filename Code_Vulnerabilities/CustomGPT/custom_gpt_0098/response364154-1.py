
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extract keys and values from the dictionary
x = list(freq.keys())
y = list(freq.values())

# Create the bar chart
plt.bar(x, y)

# Label the axes
plt.xlabel('Keys')
plt.ylabel('Values')

# Title of the plot
plt.title('Histogram of Frequency Data')

# Show the plot
plt.xticks(x)  # Ensure all keys are shown on x-axis
plt.show()
