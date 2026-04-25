
import numpy as np
from collections import Counter

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 in intervals of 10

# Count occurrences in each bin
hist = Counter()

for value in a:
    # Find the appropriate bin
    bin_index = np.digitize(value, bins) - 1
    if bin_index < len(bins):
        hist[bins[bin_index]] += 1

# Prepare output in table format
print("bins   data")
for bin_start in bins:
    print(f"{bin_start:3d}   {hist[bin_start]}")

