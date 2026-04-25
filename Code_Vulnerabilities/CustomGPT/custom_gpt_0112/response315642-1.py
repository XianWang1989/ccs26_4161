
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 101, 10)

# Compute the histogram
hist, bin_edges = np.histogram(a, bins=bins)

# Create a DataFrame for better formatting
data = {'Bins': bin_edges[:-1], 'Count': hist}
df = pd.DataFrame(data)

# Display the result
print(df)
