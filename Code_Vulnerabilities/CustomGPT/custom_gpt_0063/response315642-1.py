
import numpy as np
from collections import defaultdict

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 in steps of 10
bin_counts = defaultdict(int)

# Count the occurrences in each bin
for value in a:
    bin_index = np.digitize(value, bins) - 1
    if bin_index >= 0 and bin_index < len(bins) - 1:
        bin_counts[bins[bin_index]] += 1
    elif bin_index == len(bins) - 1:  # Edge case for the last bin
        bin_counts[bins[-1]] += 1

# Print the output in table format
print("bin\tcount")
for bin in bins:
    print(f"{bin}\t{bin_counts[bin]}") 
