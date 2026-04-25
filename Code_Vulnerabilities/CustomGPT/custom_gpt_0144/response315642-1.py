import numpy as np
from collections import Counter

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bin edges (0 to 100 with step of 10)
bins = np.arange(10, 110, 10)

# Digitize the data
indices = np.digitize(a, bins, right=True)

# Count occurrences in each bin
count = Counter(indices)

# Print bin and count
print("Bin\tCount")
for i, b in enumerate(bins, 1):
    print(f"{b}\t{count.get(i, 0)}")
