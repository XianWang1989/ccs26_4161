
import matplotlib.pyplot as plt

# Your dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Prepare data for plotting
keys = list(freq.keys())
values = list(freq.values())

# Create a bar chart
plt.bar(keys, values)

# Label the axes
plt.xlabel('Keys')
plt.ylabel('Frequency')
plt.title('Histogram of Frequencies')

# Show the plot
plt.xticks(keys)  # Ensure all keys are shown on the X-axis
plt.show()
