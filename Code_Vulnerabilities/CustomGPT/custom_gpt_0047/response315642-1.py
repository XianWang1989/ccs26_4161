
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 110, 10)

# Use numpy's histogram function
hist, bin_edges = np.histogram(a, bins=bins)

# Prepare the output data in table format
bin_centers = bin_edges[:-1]  # Get the left side of the bins
output_data = pd.DataFrame({'bins': bin_centers, 'counts': hist})

# Display the result
print(output_data)
