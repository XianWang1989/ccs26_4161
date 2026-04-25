
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 with a width of 10

# Count values in each bin
counts, _ = np.histogram(a, bins=bins)

# Create a DataFrame for better formatting
bin_labels = bins[:-1]  # Get the left edge of the bins for labeling
hist_data = pd.DataFrame({'bins': bin_labels, 'counts': counts})

# Display the histogram data
print(hist_data)
