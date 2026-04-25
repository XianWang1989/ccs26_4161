
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(10, 110, 10)  # Binning from 10 to 100 in steps of 10

# Create histogram
hist, _ = np.histogram(a, bins=bins)

# Prepare table format
bin_centers = bins[:-1]  # bin centers
output = pd.DataFrame({'Bins': bin_centers, 'Counts': hist})

# Display the output
print(output.to_string(index=False))
