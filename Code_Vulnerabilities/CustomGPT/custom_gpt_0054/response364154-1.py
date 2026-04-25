
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extract the keys and values
x_labels = list(freq.keys())
y_values = list(freq.values())

# Create the bar chart
plt.bar(x_labels, y_values)

# Label the axes
plt.xlabel('Keys (1 to 43)')
plt.ylabel('Frequency')

# Title of the chart
plt.title('Histogram of Frequencies')

# Show the plot
plt.xticks(x_labels)  # Ensure all keys are displayed on the X axis
plt.show()
