
import matplotlib.pyplot as plt

# Sample frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Prepare data for plotting
x = list(freq.keys())  # X-axis values (keys)
y = list(freq.values())  # Y-axis values (values)

# Create the bar chart
plt.bar(x, y)

# Label the axes
plt.xlabel('Keys')
plt.ylabel('Frequency')
plt.title('Histogram from Dictionary Data')

# Show the plot
plt.xticks(x)  # Ensure all keys are shown on x-axis
plt.show()
