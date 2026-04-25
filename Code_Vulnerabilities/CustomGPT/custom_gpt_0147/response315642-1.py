
import numpy as np

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins range and create bins
bins = np.arange(10, 110, 10)  # Bins from 10 to 100

# Count occurrences in each bin
hist, bin_edges = np.histogram(a, bins=bins)

# Printing the result in the desired format
print("bins data")
for i in range(len(hist)):
    print(f"{bin_edges[i]}  {hist[i]}")
