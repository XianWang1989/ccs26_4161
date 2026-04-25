
import matplotlib.pyplot as plt

# Frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extract keys and values
x_labels = list(freq.keys())
y_values = list(freq.values())

# Create a bar chart
plt.bar(x_labels, y_values, color='skyblue')

# Labeling the axes and title
plt.xlabel('Keys')
plt.ylabel('Values')
plt.title('Histogram of Frequency Data')

# Show grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.xticks(x_labels)  # Ensuring each key is marked on the x-axis
plt.show()
