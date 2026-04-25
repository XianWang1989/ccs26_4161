
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Getting the keys and values from the dictionary
x = list(freq.keys())
y = list(freq.values())

# Creating the bar chart
plt.bar(x, y)

# Adding labels and title
plt.xlabel('Keys')
plt.ylabel('Values')
plt.title('Bar Chart of Frequency')

# Displaying the chart
plt.xticks(x)  # Ensuring all keys are included on the x-axis
plt.show()
