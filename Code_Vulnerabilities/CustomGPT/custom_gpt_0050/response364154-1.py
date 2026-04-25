
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Prepare the data
x = list(freq.keys())  # X values (keys)
y = list(freq.values())  # Y values (values)

# Create the bar chart
plt.bar(x, y)

# Labeling the axes
plt.xlabel('Keys')
plt.ylabel('Frequency')
plt.title('Histogram of Frequency')

# Show the plot
plt.xticks(x)  # Show all x values
plt.show()
