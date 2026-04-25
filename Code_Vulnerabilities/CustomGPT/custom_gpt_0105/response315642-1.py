
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 101, 10)

# Use numpy's histogram function to get counts in each bin
counts, _ = np.histogram(a, bins=bins)

# Create a DataFrame for better formatting
histogram_data = pd.DataFrame({'bins': bins[:-1], 'counts': counts})

# Print as a table
print(histogram_data.to_string(index=False))
