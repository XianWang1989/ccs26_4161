
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 101, 10)

# Compute histogram
hist, bin_edges = np.histogram(a, bins=bins)

# Create a DataFrame to display bins and counts
bin_counts = pd.DataFrame({
    'bins': bin_edges[:-1],
    'counts': hist
})

# Print the result
print(bin_counts)
