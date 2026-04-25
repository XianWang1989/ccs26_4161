
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 101, 10)

# Create a histogram
hist, bin_edges = np.histogram(a, bins=bins)

# Prepare data for output
data = {'Bins': bin_edges[:-1], 'Counts': hist}
df = pd.DataFrame(data)

# Display the resulting table
print(df)
