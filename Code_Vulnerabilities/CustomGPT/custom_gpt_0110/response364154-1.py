
import matplotlib.pyplot as plt

# Your frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extracting keys and values from the dictionary
keys = list(freq.keys())
values = list(freq.values())

# Creating the bar chart
plt.bar(keys, values, color='skyblue')

# Adding titles and labels
plt.title('Histogram of Frequencies')
plt.xlabel('Keys')
plt.ylabel('Values')

# Displaying the plot
plt.xticks(keys)  # Ensure all keys are displayed on the X axis
plt.show()
