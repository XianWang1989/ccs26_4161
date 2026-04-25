
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 101, 10)

# Calculate histogram
hist, _ = np.histogram(a, bins=bins)

# Create a DataFrame to format the output
bin_edges = [f"{b}" for b in bins[:-1]]  # Bin starts (0 to 90)
data = pd.DataFrame({'bins': bin_edges, 'data': hist})

# Print the result
print(data)
