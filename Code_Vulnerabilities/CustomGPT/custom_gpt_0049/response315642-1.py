
import numpy as np

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bin edges
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 with step of 10

# Compute histogram
counts, edges = np.histogram(a, bins=bins)

# Displaying the output in table format
print("Bins   Count")
for i in range(len(counts)):
    print(f"{edges[i]:<5} {counts[i]}")
