
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 in steps of 10

# Use np.histogram to calculate the frequency
hist, edges = np.histogram(a, bins=bins)

# Create a DataFrame for better display
bin_centers = [(edges[i] + edges[i+1]) / 2 for i in range(len(edges)-1)]
df = pd.DataFrame({'bins': bin_centers, 'data': hist})

# Display the result
print(df)
