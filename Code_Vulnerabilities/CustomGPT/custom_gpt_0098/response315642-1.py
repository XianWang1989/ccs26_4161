
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 110, 10)

# Count occurrences in each bin
counts, _ = np.histogram(a, bins=bins)

# Prepare data for DataFrame
bin_edges = bins[:-1]  # Get the left edges of the bins
data = {'bins': bin_edges, 'data': counts}

# Create a DataFrame
df = pd.DataFrame(data)

# Print the result
print(df)
