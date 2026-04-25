
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 110, 10)  # Bins from 0 to 100 with a width of 10

# Calculate the histogram
hist, bin_edges = np.histogram(a, bins=bins)

# Prepare the output in table format
output = pd.DataFrame({
    'Bins': bin_edges[:-1],  # Start of the bin
    'Frequency': hist  # Frequency count
})

# Print the result
print(output.to_string(index=False))
