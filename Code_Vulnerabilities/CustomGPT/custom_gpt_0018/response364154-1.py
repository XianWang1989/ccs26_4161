
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extract keys and values
keys = list(freq.keys())
values = list(freq.values())

# Create the bar chart
plt.bar(keys, values)

# Adding titles and labels
plt.title('Histogram of Frequencies')
plt.xlabel('Keys')
plt.ylabel('Values')

# Show the plot
plt.xticks(keys)  # Make sure all keys are shown in X-axis
plt.show()
