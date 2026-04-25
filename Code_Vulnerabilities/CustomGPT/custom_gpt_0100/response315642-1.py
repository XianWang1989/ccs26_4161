
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 110, 10)

# Calculate histogram
hist, bin_edges = np.histogram(a, bins=bins)

# Create a DataFrame for better formatting
hist_data = pd.DataFrame({
    'Bins': bin_edges[:-1],
    'Counts': hist
})

# Print the table
print(hist_data.to_string(index=False))
