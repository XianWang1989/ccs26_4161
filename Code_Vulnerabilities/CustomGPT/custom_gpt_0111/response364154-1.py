
import matplotlib.pyplot as plt

# Your dictionary data
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Prepare data for plotting
keys = list(freq.keys())
values = list(freq.values())

# Create the bar chart
plt.bar(keys, values)

# Set labels and title
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.title('Histogram of Frequency Distribution')

# Show the plot
plt.xticks(keys)  # Show all keys on the X-axis
plt.show()
