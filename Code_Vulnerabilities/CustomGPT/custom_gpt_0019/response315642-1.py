
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 with a width of 10

# Use np.histogram to count the values in each bin
hist, edges = np.histogram(a, bins=bins)

# Create a dataframe for better visualization
bin_centers = (edges[:-1] + edges[1:]) / 2
hist_table = pd.DataFrame({'bin': bin_centers, 'count': hist})

# Format the output
result = hist_table.set_index('bin').reindex(np.arange(10, 101, 10), fill_value=0)
print(result)
