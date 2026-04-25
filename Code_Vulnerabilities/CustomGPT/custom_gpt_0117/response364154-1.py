
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Creating lists for keys and values
keys = list(freq.keys())
values = list(freq.values())

# Creating the bar chart
plt.bar(keys, values)

# Adding titles and labels
plt.title('Histogram of Frequencies')
plt.xlabel('Keys')
plt.ylabel('Values')

# Display the plot
plt.xticks(keys)  # Show all x-ticks
plt.grid(axis='y')  # Optional: add gridlines for better readability
plt.show()
