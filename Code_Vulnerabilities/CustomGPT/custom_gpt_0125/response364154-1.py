
import matplotlib.pyplot as plt

# Sample frequency dictionary
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Extracting keys and values
keys = sorted(freq.keys())
values = [freq[key] for key in keys]

# Creating the bar chart
plt.bar(keys, values)

# Adding titles and labels
plt.title("Histogram of Frequencies")
plt.xlabel("Keys")
plt.ylabel("Values")

# Show the plot
plt.show()
