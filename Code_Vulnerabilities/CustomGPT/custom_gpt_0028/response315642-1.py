
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 101, 10)  # Create bins from 0 to 100 with a width of 10

# Use numpy's histogram function to count the occurrences in each bin
counts, _ = np.histogram(a, bins=bins)

# Prepare the output as a DataFrame
bin_edges = bins[:-1]  # Get the left edge of each bin
df = pd.DataFrame({'bins data': bin_edges, 'value': counts})

# Display the result
print(df)
