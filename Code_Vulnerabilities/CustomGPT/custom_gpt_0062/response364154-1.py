
import matplotlib.pyplot as plt

# Your frequency data
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extract keys and values
x = list(freq.keys())
y = list(freq.values())

# Create a bar chart
plt.bar(x, y)

# Add labels and title
plt.xlabel('Keys')
plt.ylabel('Values')
plt.title('Frequency Histogram')

# Show the plot
plt.xticks(x)  # Ensure all keys are shown on the x-axis
plt.show()
