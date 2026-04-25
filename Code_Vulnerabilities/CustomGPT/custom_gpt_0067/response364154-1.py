
import matplotlib.pyplot as plt

# Your frequency data
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extracting keys and values
keys = list(freq.keys())
values = list(freq.values())

# Creating the bar chart
plt.bar(keys, values)

# Adding titles and labels
plt.title('Histogram of Frequencies')
plt.xlabel('Numbers')
plt.ylabel('Frequency')

# Display the plot
plt.xticks(keys)  # Set x-ticks to show all keys
plt.show()
