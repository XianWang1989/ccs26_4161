
import matplotlib.pyplot as plt

# Your frequency data
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extracting keys and values
keys = list(freq.keys())
values = list(freq.values())

# Creating the bar chart
plt.bar(keys, values)

# Adding labels and title
plt.xlabel('Keys')
plt.ylabel('Frequency')
plt.title('Frequency Histogram')

# Displaying the plot
plt.xticks(keys)  # Ensuring all keys are displayed on x-axis
plt.show()
