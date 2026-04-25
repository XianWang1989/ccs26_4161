
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extract keys and values
x = list(freq.keys())
y = list(freq.values())

# Create the bar chart
plt.bar(x, y)

# Add labels and title
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Frequency Distribution')

# Show grid for better readability
plt.grid(axis='y')

# Display the plot
plt.show()
