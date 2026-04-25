
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Prepare data for plotting
keys = list(freq.keys())                  # Get the keys for the X-axis
values = list(freq.values())              # Get the values for the Y-axis

# Create the bar chart
plt.bar(keys, values)

# Adding titles and labels
plt.title('Histogram from Dictionary Data')
plt.xlabel('Keys')
plt.ylabel('Values')

# Display the graph
plt.xticks(keys)  # Ensure all keys are shown on the X-axis
plt.show()
