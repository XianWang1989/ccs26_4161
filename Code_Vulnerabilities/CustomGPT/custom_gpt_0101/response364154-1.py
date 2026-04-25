
import matplotlib.pyplot as plt

# Given frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extract keys and values
x = list(freq.keys())
y = list(freq.values())

# Create bar chart
plt.bar(x, y)

# Add titles and labels
plt.title('Histogram of Frequencies')
plt.xlabel('Keys')
plt.ylabel('Values')

# Show plot
plt.xticks(x)  # Ensure all keys are shown on X-axis
plt.show()
