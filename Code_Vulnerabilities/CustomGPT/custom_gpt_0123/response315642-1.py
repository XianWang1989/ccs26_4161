
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 110, 10)

# Count the values in each bin
hist, edges = np.histogram(a, bins=bins)

# Create a DataFrame for better formatting
bin_data = pd.DataFrame({'bins': edges[:-1], 'data': hist})

# Displaying the output
print(bin_data)
