
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 110, 10)  # Bins from 0 to 100 with a width of 10

# Use numpy to calculate histogram data
hist, edges = np.histogram(a, bins=bins)

# Create a DataFrame for better visualization
bin_data = pd.DataFrame({'bins': edges[:-1], 'data': hist})

# Display the result
print(bin_data)
