
import matplotlib.pyplot as plt

# Your frequency data
freq = {1: 1000, 2: 980, 4: 560, 5: 400, 10: 250, 20: 150, 30: 50, 40: 3, 41: 1, 43: 1}

# Extracting keys and values
x = list(freq.keys())
y = list(freq.values())

# Creating the bar chart
plt.bar(x, y)

# Adding title and labels
plt.title("Frequency Histogram")
plt.xlabel("Keys")
plt.ylabel("Values")

# Setting the X axis limits if needed (optional)
plt.xlim(min(x) - 1, max(x) + 1)

# Showing the plot
plt.show()
