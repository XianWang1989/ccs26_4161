
import matplotlib.pyplot as plt

# Given frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extract keys and values from the dictionary
x = list(freq.keys())  # X axis values (keys)
y = list(freq.values())  # Y axis values (values)

# Create a bar chart
plt.bar(x, y)

# Labeling the chart
plt.xlabel('Numbers')
plt.ylabel('Frequency')
plt.title('Bar chart of Frequency Distribution')

# Show the plot
plt.xticks(x)  # show all keys on the x-axis
plt.show()
