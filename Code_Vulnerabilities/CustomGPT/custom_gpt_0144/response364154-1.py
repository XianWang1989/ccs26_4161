import matplotlib.pyplot as plt

# Your frequency data
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Sort keys for consistent X-axis order
keys = sorted(freq.keys())
values = [freq.get(k, 0) for k in keys]

# Plotting the bar chart
plt.bar(keys, values)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Frequency Histogram')
plt.xticks(keys, rotation=90)  # Rotate X labels if too many
plt.tight_layout()  # Adjust layout to fit labels
plt.show()
