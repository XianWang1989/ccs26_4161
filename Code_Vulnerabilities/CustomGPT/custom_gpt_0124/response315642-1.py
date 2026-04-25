
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 101, 10)

# Use numpy's histogram function to count values in each bin
hist, edges = np.histogram(a, bins=bins)

# Create a DataFrame to display the results
bin_centers = (edges[:-1] + edges[1:]) / 2
output = pd.DataFrame({'bins': bin_centers, 'data': hist})

# Display output
print(output)
