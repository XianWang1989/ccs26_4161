
import matplotlib.pyplot as plt

# Your frequency data
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Prepare data for plotting
x = list(freq.keys())
y = list(freq.values())

# Create the bar chart
plt.bar(x, y)

# Set labels and title
plt.xlabel('Keys')
plt.ylabel('Frequency')
plt.title('Histogram of Frequencies')

# Show the plot
plt.xticks(x)  # Ensure all keys are shown on the X-axis
plt.show()
