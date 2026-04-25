
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(10, 110, 10)  # Bins from 10 to 100 with a width of 10

# Compute counts in each bin
counts, _ = np.histogram(a, bins=bins)

# Create a DataFrame to display bins and counts
histogram_data = pd.DataFrame({'Bins': bins[:-1], 'Counts': counts})

# Display the result
print(histogram_data)
