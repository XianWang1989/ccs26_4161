
import matplotlib.pyplot as plt

# Your frequency data
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Prepare the data
keys = list(freq.keys())
values = list(freq.values())

# Create the bar chart
plt.bar(keys, values)

# Adding titles and labels
plt.title('Frequency Histogram')
plt.xlabel('Keys')
plt.ylabel('Values')

# Display the chart
plt.xticks(keys)  # Ensure all keys appear on the X axis
plt.show()
