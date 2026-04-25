
import matplotlib.pyplot as plt

# Your frequency data
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Prepare data for plotting
x = list(freq.keys())  # X-axis values (keys)
y = list(freq.values())  # Y-axis values (frequencies)

# Create the bar chart
plt.bar(x, y)

# Add titles and labels
plt.title('Frequency Histogram')
plt.xlabel('Keys')
plt.ylabel('Frequency')

# Show grid for better readability
plt.grid(axis='y')

# Display the plot
plt.xticks(x)  # Ensure all keys are displayed on the X-axis
plt.show()
