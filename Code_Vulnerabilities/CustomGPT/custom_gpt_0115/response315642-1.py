
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 with a width of 10

# Histogram calculation
hist, bin_edges = np.histogram(a, bins=bins)

# Create a DataFrame for better presentation
bin_centers = bin_edges[:-1]  # Get the left edges of the bins
data = pd.DataFrame({'bins': bin_centers, 'data': hist})

# Display the result
print(data)
