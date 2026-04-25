
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 in steps of 10

# Count the occurrences in each bin
hist, _ = np.histogram(a, bins=bins)

# Create a DataFrame for better visualization
bin_labels = bins[:-1]  # Exclude the last bin edge
hist_data = pd.DataFrame({
    'bins': bin_labels,
    'data': hist
})

# Display the result
print(hist_data)
