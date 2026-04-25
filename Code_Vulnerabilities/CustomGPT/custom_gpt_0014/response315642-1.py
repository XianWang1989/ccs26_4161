
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(10, 110, 10)  # Bins from 10 to 100

# Create histogram
hist, edges = np.histogram(a, bins=bins)

# Create a DataFrame for better formatting
bin_centers = edges[:-1]  # Get the bin centers
data = pd.DataFrame({'bins': bin_centers, 'counts': hist})

# Print the result
print(data)
