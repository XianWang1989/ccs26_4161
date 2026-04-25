
import matplotlib.pyplot as plt

# Your frequency data
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Create lists from the dictionary for plotting
x = list(freq.keys())  # X-axis values (keys)
y = list(freq.values())  # Y-axis values (frequencies)

# Create a bar chart
plt.bar(x, y, color='blue')

# Add labels and title
plt.xlabel('Numbers')
plt.ylabel('Frequency')
plt.title('Histogram of Frequencies')

# Show the plot
plt.xticks(x)  # Show all keys on the X-axis
plt.show()
