
import matplotlib.pyplot as plt

# Your frequency data
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Separate the keys and values
keys = freq.keys()
values = freq.values()

# Create the bar chart
plt.bar(keys, values)

# Add labels and title
plt.xlabel('Keys')
plt.ylabel('Values')
plt.title('Bar Chart from Dictionary Data')

# Show the plot
plt.xticks(keys)  # To show all keys on the x-axis
plt.show()
