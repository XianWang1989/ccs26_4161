
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100, with a width of 10

# Calculate histogram
hist, bin_edges = np.histogram(a, bins=bins)

# Prepare data for table format
bin_centers = bin_edges[:-1] + (bin_edges[1] - bin_edges[0]) / 2
table_data = pd.DataFrame({'bins': bin_centers, 'data': hist})

# Display the table
print(table_data.to_string(index=False))
