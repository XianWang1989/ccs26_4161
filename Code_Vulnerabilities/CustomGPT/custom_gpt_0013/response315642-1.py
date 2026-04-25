
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 101, 10)

# Calculate histogram
hist, _ = np.histogram(a, bins=bins)

# Prepare data for output
bin_centers = bins[:-1]  # Bin centers
data = pd.DataFrame({'Bins': bin_centers, 'Counts': hist})

# Display data in table format
print(data)
