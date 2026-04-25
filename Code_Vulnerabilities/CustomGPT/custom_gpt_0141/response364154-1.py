
import matplotlib.pyplot as plt

# Frequency data
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extract keys and values
keys = list(freq.keys())
values = list(freq.values())

# Create a bar chart
plt.figure(figsize=(10, 6))  # Set the figure size
plt.bar(keys, values, color='blue')  # Create bars

# Add titles and labels
plt.title('Frequency Histogram')
plt.xlabel('Keys')
plt.ylabel('Values')
plt.xticks(keys)  # Set X-axis ticks to be the keys

# Show the plot
plt.grid(axis='y', linestyle='--')
plt.show()
