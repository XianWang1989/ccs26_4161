
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 5: 400, 6: 300, 15: 150, 20: 100, 
        30: 80, 35: 50, 40: 3, 41: 1, 43: 1}

# Extract keys and values for plotting
x = list(freq.keys())
y = list(freq.values())

# Create the bar chart
plt.bar(x, y)

# Adding title and labels
plt.title('Histogram of Frequency Data')
plt.xlabel('Keys (X-axis)')
plt.ylabel('Values (Y-axis)')

# Show the plot
plt.xticks(x)  # make sure each key is shown on the x-axis
plt.show()
