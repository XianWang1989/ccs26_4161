
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 in steps of 10

# Use np.histogram to get the counts for each bin
hist, edges = np.histogram(a, bins)

# Create a DataFrame for better formatting
bin_centers = edges[:-1]  # Get the lower edges of bins
bin_data = pd.DataFrame({'bins': bin_centers, 'data': hist})

# Print the result
print(bin_data.to_string(index=False))
