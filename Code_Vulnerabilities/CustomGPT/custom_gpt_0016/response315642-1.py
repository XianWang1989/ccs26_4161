
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bin edges
bins = np.arange(10, 110, 10)  # This creates bins from 10 to 100 with a step of 10

# Use np.histogram to count the occurrences in each bin
hist, edges = np.histogram(a, bins)

# Create a DataFrame to make it more presentable
bin_data = pd.DataFrame({
    'bins': edges[:-1],
    'data': hist,
})

# Print the output in table format
print(bin_data)
