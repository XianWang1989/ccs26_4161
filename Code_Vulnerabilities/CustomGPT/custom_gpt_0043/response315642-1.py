
import numpy as np

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 110, 10)  # Bins from 0 to 100 with a width of 10
# Use `np.histogram` to compute the histogram
hist, bin_edges = np.histogram(a, bins=bins)

# Print header
print("bins data")
print()

# Print bin counts in the desired format
for i in range(len(hist)):
    print(f"{bin_edges[i]}  {hist[i]}")
