
import numpy as np
from collections import Counter

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 110, 10)  # From 0 to 100 in steps of 10

# Use numpy's histogram function to count data in bins
hist, bin_edges = np.histogram(a, bins=bins)

# Create a dictionary to format the output
bin_counts = {int(bin_edge): count for bin_edge, count in zip(bin_edges[:-1], hist)}

# Print the output in the desired format
print("bins data")
for bin_start in range(10, 101, 10):
    count = bin_counts.get(bin_start, 0)
    print(f"{bin_start}  {count}")
