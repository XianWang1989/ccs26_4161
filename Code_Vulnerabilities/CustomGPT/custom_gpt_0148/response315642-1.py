
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 110, 10)  # Bins from 0 to 100 with a width of 10

# Calculate the histogram
hist, _ = np.histogram(a, bins)

# Prepare the bin labels
bin_labels = bins[:-1]  # Start of each bin

# Create a DataFrame for better visualization
hist_df = pd.DataFrame({'bins': bin_labels, 'data': hist})

# Print the result
print(hist_df)
