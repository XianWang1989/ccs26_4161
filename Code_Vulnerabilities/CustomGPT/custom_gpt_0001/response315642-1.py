
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(10, 110, 10)  # Create bins from 10 to 100 with a step of 10

# Count occurrences in each bin
counts, _ = np.histogram(a, bins=bins)

# Create a DataFrame for better display
bins_data = pd.DataFrame({'bin_start': bins[:-1], 'count': counts})

# Format and display the output
print("bins data")
for index, row in bins_data.iterrows():
    print(f"{row['bin_start']:2d}  {row['count']}")
