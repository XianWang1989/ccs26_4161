
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(10, 101, 10)  # Bins from 10 to 100 (inclusive) with a step of 10

# Use numpy's histogram function
hist, bin_edges = np.histogram(a, bins=bins)

# Create a DataFrame to display the results
bin_centers = bin_edges[:-1]  # Get the left edges for bin centers
results = pd.DataFrame({'bins': bin_centers, 'data': hist})

# Display the result table
print(results.to_string(index=False))
