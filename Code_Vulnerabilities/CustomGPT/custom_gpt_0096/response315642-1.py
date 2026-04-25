
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(10, 110, 10)  # Bins from 10 to 100 with a step of 10

# Calculate histogram
hist, bin_edges = np.histogram(a, bins=bins)

# Prepare data for output
output_data = pd.DataFrame({'bins': bins[:-1], 'count': hist})

# Display the result
print(output_data.to_string(index=False))
