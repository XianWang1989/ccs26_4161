
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extracting keys and values
x = list(freq.keys())
y = list(freq.values())

# Creating the bar chart
plt.bar(x, y)

# Adding labels and title
plt.xlabel('Keys')
plt.ylabel('Frequency')
plt.title('Frequency Histogram')

# Show the plot
plt.xticks(x)  # Ensuring all keys are shown on X axis
plt.show()
