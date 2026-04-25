
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(10, 101, 10)  # From 10 to 100 with a step of 10

# Digitize data into bins
counts, _ = np.histogram(a, bins=bins)

# Create a DataFrame to show bins and counts
df = pd.DataFrame({'bins': bins[:-1], 'data': counts})

# Display the DataFrame
print(df)
