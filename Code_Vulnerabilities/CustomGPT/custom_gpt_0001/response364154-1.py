
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extract keys and values from the dictionary
x = list(freq.keys())
y = list(freq.values())

# Create the bar chart
plt.bar(x, y, color='blue')

# Add labels and title
plt.xlabel('Keys')
plt.ylabel('Values')
plt.title('Histogram of Frequency')

# Show the plot
plt.xticks(x)  # Ensures that each key is shown on the x-axis
plt.show()
