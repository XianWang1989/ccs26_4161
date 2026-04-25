
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 110, 10)  # Bins from 0 to 100 with a step of 10

# Calculate the histogram
counts, _ = np.histogram(a, bins=bins)

# Prepare the data for DataFrame
data = {'bins': bins[:-1], 'data': counts}  # Exclude the last bin edge for correct counts
df = pd.DataFrame(data)

# Print the output in table format
print(df.to_string(index=False))
