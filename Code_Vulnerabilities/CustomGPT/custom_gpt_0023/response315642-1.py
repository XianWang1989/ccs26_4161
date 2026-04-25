
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 with a width of 10

# Digitize the data to find the bin each value belongs to
counts, _ = np.histogram(a, bins=bins)

# Create a DataFrame for better visualization
bin_labels = bins[:-1]  # Ignore the last bin edge for labels
bin_data = pd.DataFrame({
    'bins': bin_labels,
    'data': counts
})

# Display the output in table format
print(bin_data)
