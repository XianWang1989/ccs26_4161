
import matplotlib.pyplot as plt

# Given frequency dictionary
freq = {
    1: 1000, 2: 980, 4: 560, 5: 420, 6: 200,
    7: 150, 8: 90, 9: 75, 10: 55, 11: 40,
    12: 30, 13: 20, 14: 14, 15: 10, 16: 9,
    17: 8, 18: 6, 19: 5, 20: 4, 21: 2,
    22: 2, 23: 1, 24: 1, 25: 1, 26: 1,
    27: 1, 28: 1, 29: 1, 30: 1, 31: 1,
    32: 1, 33: 1, 34: 1, 35: 1, 36: 1,
    37: 1, 38: 1, 39: 1, 40: 3, 41: 1, 43: 1
}

# Create a bar chart
plt.bar(freq.keys(), freq.values())

# Set the title and labels
plt.title('Frequency Histogram')
plt.xlabel('Keys')
plt.ylabel('Values')

# Show the plot
plt.xticks(range(1, 44))  # Optionally set x-ticks for every number between 1 and 43
plt.show()
