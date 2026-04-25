
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Create a bar plot
plt.bar(freq.keys(), freq.values())

# Adding labels and title
plt.xlabel('Keys')
plt.ylabel('Values')
plt.title('Bar Chart of Frequency Data')

# Show the plot
plt.xticks(range(1, 44))  # Set x ticks from 1 to 43
plt.grid(axis='y')  # Add gridlines for better readability
plt.show()
