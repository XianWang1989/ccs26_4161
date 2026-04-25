
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extract keys and values
keys = list(freq.keys())
values = list(freq.values())

# Create bar chart
plt.bar(keys, values)

# Adding labels and title
plt.xlabel('Keys')
plt.ylabel('Frequency')
plt.title('Frequency Distribution')

# Show the plot
plt.xticks(keys)  # Ensure all keys are shown on the x-axis
plt.show()
