
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 110, 10)

# Calculate histogram
hist, edges = np.histogram(a, bins=bins)

# Prepare output in table format
bin_centers = edges[:-1]  # Bin centers
df = pd.DataFrame({'bins': bin_centers, 'data': hist})

# Display the output
print(df)
