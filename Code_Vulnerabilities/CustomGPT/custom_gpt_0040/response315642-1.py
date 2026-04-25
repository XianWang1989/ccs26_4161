
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bin edges
bins = np.arange(0, 110, 10)  # Bins from 0 to 100, step by 10

# Use numpy's histogram to get counts in bins
counts, _ = np.histogram(a, bins)

# Create a DataFrame for better visualization
histogram_df = pd.DataFrame({'bins': bins[:-1], 'data': counts})

# Display the table
print(histogram_df)
