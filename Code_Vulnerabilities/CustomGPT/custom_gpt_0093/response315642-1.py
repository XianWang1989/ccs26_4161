
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 101, 10)

# Count the occurrences in each bin
counts, edges = np.histogram(a, bins=bins)

# Create a DataFrame for better visualization
histogram_data = pd.DataFrame({
    'bins': edges[:-1],
    'counts': counts
})

# Display the result
print(histogram_data)
