
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Create bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 with a width of 10

# Calculate histogram
hist, edges = np.histogram(a, bins=bins)

# Create a dataframe to hold the results
bin_centers = (edges[:-1] + edges[1:]) / 2  # Calculate bin centers
data = pd.DataFrame({'bins': bin_centers, 'count': hist})

# Print the result in table format
print(data)
