
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 with a step of 10

# Create a histogram
hist, bin_edges = np.histogram(a, bins=bins)

# Prepare output in table format
output = pd.DataFrame({
    'bins': bin_edges[:-1],  # exclude the last edge for bin representation
    'data': hist
})

# Display the output dataframe
print(output)
