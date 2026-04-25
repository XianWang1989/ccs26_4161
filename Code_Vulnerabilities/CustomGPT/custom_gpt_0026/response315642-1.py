
import numpy as np
from collections import Counter

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Create bins (adjust the range and width as needed)
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 with a width of 10

# Count occurrences in bins
hist, _ = np.histogram(a, bins=bins)

# Prepare output in table format
print("bins data")
for i in range(len(hist)):
    print(f"{bins[i]}  {hist[i]}")
