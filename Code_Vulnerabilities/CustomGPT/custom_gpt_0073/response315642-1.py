
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bin edges
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 with a step of 10

# Use np.histogram to count occurrences in each bin
hist, edges = np.histogram(a, bins=bins)

# Prepare the output in table format
output = pd.DataFrame({'bins': edges[:-1], 'data': hist})

print(output)
