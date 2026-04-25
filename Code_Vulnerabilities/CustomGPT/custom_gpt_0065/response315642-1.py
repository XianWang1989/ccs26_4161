
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 101, 10)  # Bins: 0-10, 10-20, ..., 90-100

# Count occurrences in each bin
hist, edges = np.histogram(a, bins=bins)

# Prepare output in table format
bin_centers = edges[:-1]  # Get bin starting points
data = pd.DataFrame({'bins': bin_centers, 'data': hist})

# Print the result
print(data)
