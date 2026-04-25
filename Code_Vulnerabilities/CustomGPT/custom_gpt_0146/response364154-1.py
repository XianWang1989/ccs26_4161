
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 5: 400, 10: 250, 20: 100, 30: 50, 40: 3, 41: 1, 43: 1}

# Extracting the keys and values for plotting
keys = list(freq.keys())
values = list(freq.values())

# Creating the bar chart
plt.bar(keys, values)

# Adding titles and labels
plt.title('Histogram of Frequency')
plt.xlabel('Keys')
plt.ylabel('Values')

# Show the plot
plt.xticks(keys)  # Ensures that all keys are shown on the x-axis
plt.grid(axis='y')  # Optional: Adds grid lines for better readability
plt.show()
