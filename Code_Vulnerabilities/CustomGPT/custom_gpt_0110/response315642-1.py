
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 110, 10)  # Bins from 0 to 100 with a width of 10

# Create the histogram
hist, bin_edges = np.histogram(a, bins=bins)

# Create a DataFrame for better display
hist_df = pd.DataFrame({'bins': bin_edges[:-1], 'value': hist})

# Print the result
print(hist_df)
