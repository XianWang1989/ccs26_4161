
import numpy as np
from collections import defaultdict

# Given input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bin width and start/stop for bins
bin_width = 10
start = 10
stop = 100

# Create bins
bins = np.arange(start, stop + bin_width, bin_width)

# Count occurrences in each bin
bin_counts = defaultdict(int)

for value in a:
    # Find the right bin for each value
    for i in range(len(bins) - 1):
        if bins[i] <= value < bins[i+1]:
            bin_counts[bins[i]] += 1
            break

# Print the results in the desired format
print("bins data")
for bin in range(start, stop + bin_width, bin_width):
    count = bin_counts[bin]
    print(f"{bin}  {count}")
