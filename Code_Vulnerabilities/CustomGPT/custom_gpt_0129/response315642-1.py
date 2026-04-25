
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 110, 10)  # Create bins from 0 to 100 with a width of 10

# Use np.histogram to get the count of values in each bin
hist, bin_edges = np.histogram(a, bins=bins)

# Convert bin edges to bin start for easier readability and create a DataFrame
bin_centers = bin_edges[:-1]  # Get the left edges of the bins for the bin centers
output_df = pd.DataFrame({'bins': bin_centers, 'data': hist})

# Print the output in the desired format
for index, row in output_df.iterrows():
    print(f"{row['bins']:>3}  {row['data']}")
