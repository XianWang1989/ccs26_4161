
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extract keys and values
keys = list(freq.keys())
values = list(freq.values())

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(keys, values, color='blue')
plt.xlabel('Keys')
plt.ylabel('Values')
plt.title('Bar Chart of Frequency Data')
plt.xticks(keys)  # Set X-ticks to show all keys
plt.grid(axis='y')

# Show the plot
plt.show()
