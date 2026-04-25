
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 110, 10)  # Bins from 0 to 100 with a width of 10

# Create histogram data
hist, _ = np.histogram(a, bins)

# Create a table format
data = {'bins': bins[:-1], 'count': hist}
df = pd.DataFrame(data)

# Print the result
print(df.to_string(index=False))
