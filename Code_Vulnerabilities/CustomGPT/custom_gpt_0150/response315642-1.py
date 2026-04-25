
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 110, 10)

# Create histogram data
hist, edges = np.histogram(a, bins=bins)

# Prepare the output in table format
bins_data = pd.DataFrame({
    'bins': edges[:-1],
    'count': hist
})

# Display the histogram data
print(bins_data)
