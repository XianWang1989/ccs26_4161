
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100, interval of 10

# Create histogram
hist, _ = np.histogram(a, bins=bins)

# Prepare bin centers for output
bin_centers = bins[:-1]

# Create DataFrame for better formatting
hist_df = pd.DataFrame({'bins': bin_centers, 'data': hist})

# Print the DataFrame
print(hist_df.to_string(index=False))
