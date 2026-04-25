
import numpy as np
from collections import Counter

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 110, 10)  # Bins from 0 to 100 with a width of 10

# Count occurrences in each bin
hist, _ = np.histogram(a, bins)

# Format output
output = {bins[i]: hist[i] for i in range(len(hist))}

# Print in table format
print("bins   data")
for bin_value, count in output.items():
    print(f"{bin_value:<5} {count}")
