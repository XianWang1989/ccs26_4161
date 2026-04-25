
import numpy as np
from collections import Counter

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 with a step of 10
# Histogram data using np.histogram
hist, edges = np.histogram(a, bins=bins)

# Creating a table-like output
print("bins   count")
for i in range(len(hist)):
    print(f"{edges[i]:<6} {hist[i]}")
