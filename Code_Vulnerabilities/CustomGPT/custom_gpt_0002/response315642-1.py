
import numpy as np

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Create bins
bins = range(10, 110, 10)

# Calculate histogram
hist, edges = np.histogram(a, bins=bins)

# Print the output in table format
print("bins data")
for i in range(len(hist)):
    print(f"{edges[i]}  {hist[i]}")
