
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extract keys and values from the dictionary
keys = list(freq.keys())
values = list(freq.values())

# Create the bar chart
plt.bar(keys, values)

# Set titles and labels
plt.title("Histogram of Frequency Distribution")
plt.xlabel("Keys")
plt.ylabel("Values")

# Display the plot
plt.xticks(keys)  # Show all keys on the X-axis
plt.grid(axis='y')  # Optional: Add gridlines for better readability
plt.show()
