
import matplotlib.pyplot as plt

# Your frequency data
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extracting keys and values from the dictionary
x = list(freq.keys())
y = list(freq.values())

# Creating the bar chart
plt.bar(x, y)

# Adding labels and title
plt.xlabel('Keys')
plt.ylabel('Values')
plt.title('Histogram from Dictionary')

# Displaying the chart
plt.xticks(x)  # Ensures all keys are shown on the X-axis
plt.show()
