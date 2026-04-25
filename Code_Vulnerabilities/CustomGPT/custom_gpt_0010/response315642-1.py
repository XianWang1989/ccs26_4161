
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins you want
bins = np.arange(0, 101, 10)

# Get histogram data
hist, edges = np.histogram(a, bins=bins)

# Create a DataFrame for better display
bin_data = pd.DataFrame({'bins': edges[:-1], 'data': hist})

# Display the tabular format
print(bin_data)
