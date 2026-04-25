
import matplotlib.pyplot as plt

# Your frequency data
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extract keys and values
x = list(freq.keys())
y = list(freq.values())

# Create the bar chart
plt.bar(x, y)

# Set the labels and title
plt.xlabel('Numbers')
plt.ylabel('Frequency')
plt.title('Histogram of Frequencies')

# Display the plot
plt.xticks(x)  # Ensure all keys are shown on the x-axis
plt.show()
