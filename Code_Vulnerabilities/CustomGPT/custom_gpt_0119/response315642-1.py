
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 with step of 10

# Get histogram data
hist, bin_edges = np.histogram(a, bins=bins)

# Create a DataFrame for better visualization
data = {'bins': bin_edges[:-1], 'data': hist}
df = pd.DataFrame(data)

# Display the result
print(df)
