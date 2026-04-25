
import numpy as np

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 110, 10)  # Bins from 0 to 100, with a width of 10

# Use np.histogram to count the occurrences in each bin
hist, edges = np.histogram(a, bins=bins)

# Print the results in table format
print("bins data")
for i in range(len(hist)):
    print(f"{edges[i]}  {hist[i]}")
