
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 with a step of 10

# Calculate histogram
hist, edges = np.histogram(a, bins=bins)

# Prepare data for output
output = pd.DataFrame({
    'bins': edges[:-1],
    'data': hist
})

# Display the result
print(output)
