
import matplotlib.pyplot as plt

# Frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 5: 300, 10: 200, 20: 100, 30: 50, 40: 3, 41: 1, 43: 1}

# Extracting keys and values
keys = list(freq.keys())
values = list(freq.values())

# Creating the bar chart
plt.bar(keys, values)

# Adding labels and title
plt.xlabel('Keys')
plt.ylabel('Frequency')
plt.title('Bar Chart of Frequency Distribution')

# Show the plot
plt.xticks(keys)  # Ensure all keys are labeled on the X-axis
plt.grid(axis='y')  # Optional: Add grid lines for better readability
plt.show()
