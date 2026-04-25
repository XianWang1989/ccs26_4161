
import numpy as np
from collections import Counter

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(10, 101, 10)  # Bins from 10 to 100, with a step of 10

# Count occurrences in each bin
hist, edges = np.histogram(a, bins=bins)

# Prepare output in the desired table format
print("bins data")
for i in range(len(hist)):
    print(f"{edges[i]}  {hist[i]}")
