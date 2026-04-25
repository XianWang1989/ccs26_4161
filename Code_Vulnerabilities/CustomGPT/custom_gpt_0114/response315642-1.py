
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bin edges
bins = np.arange(10, 110, 10)  # Bins from 10 to 100 with a width of 10

# Count occurrences in each bin
hist, edges = np.histogram(a, bins=bins)

# Create a DataFrame for the output
bin_centers = edges[:-1]  # Get the left edges as bin centers
output = pd.DataFrame({'bins': bin_centers, 'data': hist})

# Print the result
print(output)
