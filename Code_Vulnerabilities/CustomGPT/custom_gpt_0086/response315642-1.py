
import numpy as np
from collections import defaultdict

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(10, 110, 10)  # Bins from 10 to 100 with a width of 10
histogram = defaultdict(int)

# Count values in each bin
for value in a:
    bin_index = np.digitize(value, bins) - 1  # Find the bin index
    if bin_index < len(bins):
        histogram[bins[bin_index]] += 1  # Increment the bin count

# Print output in table format
print("bins data")
for bin_start in bins:
    print(f"{bin_start}  {histogram[bin_start]}")
