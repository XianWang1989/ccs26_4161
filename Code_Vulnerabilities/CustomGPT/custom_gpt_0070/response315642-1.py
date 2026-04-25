
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bin edges
bins = np.arange(0, 101, 10)  # Bin edges from 0 to 100 with a step of 10

# Digitize the data
counts, _ = np.histogram(a, bins)

# Create a DataFrame for bin ranges and counts
bin_labels = bins[:-1]  # Use the left edge of the bins for labeling
hist_data = pd.DataFrame({'bins': bin_labels, 'counts': counts})

# Print the histogram data
print(hist_data.to_string(index=False))
