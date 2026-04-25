
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(10, 101, 10)  # Bins from 10 to 100 with a width of 10

# Calculate histogram
hist, bin_edges = np.histogram(a, bins=bins)

# Create a DataFrame for better visualization
output = pd.DataFrame({'bins': bin_edges[:-1], 'data': hist})

# Display the output
print(output)
