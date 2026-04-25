
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 110, 10)

# Use np.histogram to get counts in bins
hist, edges = np.histogram(a, bins=bins)

# Create a DataFrame for better formatting
hist_df = pd.DataFrame({
    'bins': edges[:-1],
    'data': hist
})

# Display the DataFrame
print(hist_df)
