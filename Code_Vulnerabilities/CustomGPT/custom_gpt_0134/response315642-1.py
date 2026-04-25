
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 with a step of 10

# Use numpy's histogram to compute the counts
counts, _ = np.histogram(a, bins=bins)

# Prepare data for DataFrame
bin_edges = bins[:-1]  # Get the left edges of the bins
data = {'Bins': bin_edges, 'Counts': counts}

# Create DataFrame
df = pd.DataFrame(data)

# Display the result
print(df)
