
import numpy as np

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 101, 10)

# Compute the histogram
counts, _ = np.histogram(a, bins=bins)

# Display the output in table format
print("Bins\tData")
for i in range(len(counts)):
    print(f"{bins[i]:<5}\t{counts[i]}")
