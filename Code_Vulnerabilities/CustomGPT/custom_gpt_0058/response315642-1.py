
import numpy as np

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(10, 101, 10)  # Bins from 10 to 100 with a width of 10

# Count the occurrences in each bin
hist, bin_edges = np.histogram(a, bins=bins)

# Print the output in table format
print("bins data")
for i in range(len(hist)):
    print(f"{bins[i]}  {hist[i]}")
