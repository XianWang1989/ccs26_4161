
import numpy as np
from collections import Counter

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(10, 110, 10)

# Count values in each bin
counted = Counter(np.digitize(a, bins))

# Prepare output in the desired format
output = []
for bin_edge in bins:
    output.append(f"{bin_edge}  {counted.get(bin_edge, 0)}")

# Print formatted output
print("\n".join(output))
