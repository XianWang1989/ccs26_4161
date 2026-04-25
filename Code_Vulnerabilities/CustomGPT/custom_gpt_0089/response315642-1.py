
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bin edges
bins = np.arange(0, 101, 10)  # Create bins from 0 to 100 with a width of 10

# Use numpy's histogram function to get counts
counts, _ = np.histogram(a, bins=bins)

# Prepare bin labels
bin_labels = bins[:-1]  # Use the left edge of each bin for labeling

# Create a DataFrame to display the results
hist_table = pd.DataFrame({'bins': bin_labels, 'data': counts})

# Display the result
print(hist_table)
