
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 110, 10)

# Calculate histogram
hist, _ = np.histogram(a, bins)

# Prepare data for display
bins_data = pd.DataFrame({'bins': bins[:-1], 'count': hist})

# Displaying the result
print(bins_data)
