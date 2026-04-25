
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bin edges
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Create a histogram
hist, edges = np.histogram(a, bins=bins)

# Prepare the output in table format
table = pd.DataFrame({
    'bins': edges[:-1],  # Starting edge of each bin
    'data': hist         # Count of values in each bin
})

# Print the output
print(table)
