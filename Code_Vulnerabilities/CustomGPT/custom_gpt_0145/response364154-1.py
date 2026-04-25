
import matplotlib.pyplot as plt

# Your given frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extracting keys and values
keys = list(freq.keys())
values = list(freq.values())

# Creating the bar chart
plt.bar(keys, values, color='orange')

# Adding title and labels
plt.title('Histogram of Frequencies')
plt.xlabel('Keys')
plt.ylabel('Values')

# Display the plot
plt.xticks(keys)  # Ensure all keys are shown on the x-axis
plt.grid(axis='y')  # Optional: add a grid for better readability
plt.show()
