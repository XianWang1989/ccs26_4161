
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bin edges
bins = np.arange(10, 110, 10)  # Bins from 10 to 100 with a width of 10

# Digitize data to determine which bin each value belongs to
counts, edges = np.histogram(a, bins=bins)

# Create a DataFrame for better visualization
hist_data = pd.DataFrame({
    'bins': bins[:-1],   # left edge of each bin
    'data': counts       # counts for each bin
})

# Display the result
print(hist_data)
