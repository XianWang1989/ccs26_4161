
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 in steps of 10

# Use np.histogram to get the counts in each bin
hist, edges = np.histogram(a, bins=bins)

# Prepare the data for a table format
bin_centers = edges[:-1] + (edges[1] - edges[0]) / 2
table_data = pd.DataFrame({'bins': bin_centers, 'data': hist})

# Display the result
print(table_data.to_string(index=False))
