
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 with a width of 10

# Calculate histogram
hist, bin_edges = np.histogram(a, bins=bins)

# Prepare the output data
bin_centers = bin_edges[:-1] + 5  # Center of each bin
output_data = pd.DataFrame({'bins': bin_centers, 'data': hist})

# Display the result
print(output_data)
