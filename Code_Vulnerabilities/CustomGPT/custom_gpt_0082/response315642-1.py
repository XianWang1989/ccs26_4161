
import numpy as np
from collections import Counter

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bin edges
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 with a width of 10

# Create histogram data
hist, _ = np.histogram(a, bins=bins)

# Output in table format
print("Bins  Count")
for i in range(len(hist)):
    print(f"{bins[i]}  {hist[i]}")
