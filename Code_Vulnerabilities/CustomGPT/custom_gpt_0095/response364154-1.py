
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Sort the dictionary by keys
keys = sorted(freq.keys())
values = [freq[key] for key in keys]

# Create the bar chart
plt.bar(keys, values)

# Add labels and title
plt.xlabel('Keys')
plt.ylabel('Frequency')
plt.title('Histogram of Frequencies')

# Show the plot
plt.xticks(keys)  # Ensure all keys are shown on the x-axis
plt.grid(axis='y')  # Optional: Add gridlines for clarity
plt.show()
