
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Create histogram
hist, edges = np.histogram(a, bins=bins)

# Create a DataFrame for better visualization
df = pd.DataFrame({'bins data': edges[:-1], 'value': hist})

# Print the DataFrame
print(df)
