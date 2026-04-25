
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 with an interval of 10

# Count values in each bin
counts, _ = np.histogram(a, bins=bins)

# Prepare output in table format
output_table = pd.DataFrame({'bins': bins[:-1], 'data': counts})

# Print the output
print(output_table)
