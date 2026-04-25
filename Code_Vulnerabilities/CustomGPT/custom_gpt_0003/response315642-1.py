
import numpy as np
from collections import Counter

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Create bins
bins = np.arange(0, 101, 10)

# Count occurrences in each bin
hist, bin_edges = np.histogram(a, bins)

# Print bins data in the desired format
print("bins\tdata")
for i in range(len(hist)):
    print(f"{bins[i]}\t{hist[i]}")
