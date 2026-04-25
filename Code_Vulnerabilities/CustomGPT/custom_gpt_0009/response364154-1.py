
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Prepare data for plotting
keys = list(freq.keys())
values = list(freq.values())

# Create the bar chart
plt.bar(keys, values)

# Labeling the graph
plt.xlabel('Keys')
plt.ylabel('Frequency')
plt.title('Histogram of Frequency Dictionary')

# Display the plot
plt.xticks(keys)  # Ensure all keys are shown on the x-axis
plt.show()
