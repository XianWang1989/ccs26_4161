
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 101, 10)  # Binning from 0 to 100 in intervals of 10

# Count values in each bin
hist, edges = np.histogram(a, bins=bins)

# Prepare data for output
bin_labels = [f"{bins[i]} - {bins[i+1]}" for i in range(len(bins) - 1)]
output_data = pd.DataFrame({'bins': bin_labels, 'data': hist})

# Display result
output_data = output_data.set_index('bins')
print(output_data)
