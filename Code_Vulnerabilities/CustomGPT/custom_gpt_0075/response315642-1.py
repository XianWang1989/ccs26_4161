
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins (0 to 100, step of 10)
bins = np.arange(0, 101, 10)

# Use numpy to compute histogram
hist, edges = np.histogram(a, bins=bins)

# Create a DataFrame for better representation
df_bins = pd.DataFrame({'bins': edges[:-1], 'data': hist})

# Display the output
print(df_bins)
