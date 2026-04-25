
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100, with a width of 10

# Digitize data to find which bin each value belongs to
hist, _ = np.histogram(a, bins=bins)

# Create a DataFrame for better visualization
df = pd.DataFrame({'bins': bins[:-1], 'data': hist})

# Print the output
print(df)
