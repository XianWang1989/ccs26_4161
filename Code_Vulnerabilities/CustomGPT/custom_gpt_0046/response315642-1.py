
import numpy as np
from collections import Counter

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 101, 10)

# Count occurrences in each bin
hist, edges = np.histogram(a, bins=bins)

# Prepare output in table format
table_data = {int(edge): count for edge, count in zip(edges[:-1], hist)}

# Print the table
print("bins data")
for bin_value in range(10, 101, 10):
    print(f"{bin_value}  {table_data.get(bin_value, 0)}")
