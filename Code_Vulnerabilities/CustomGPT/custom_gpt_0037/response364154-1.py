
import matplotlib.pyplot as plt

# Given frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extracting keys and values
keys = list(freq.keys())
values = list(freq.values())

# Plotting the bar chart
plt.bar(keys, values)

# Adding labels and title
plt.xlabel('Keys')
plt.ylabel('Values')
plt.title('Histogram of Frequency Data')

# Show grid for better readability
plt.grid(axis='y')

# Display the plot
plt.show()
