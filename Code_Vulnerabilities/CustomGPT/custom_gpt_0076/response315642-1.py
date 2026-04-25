
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(10, 110, 10)  # Bins from 10 to 100 with a width of 10

# Count the occurrences in each bin
counts, _ = np.histogram(a, bins)

# Create a DataFrame for better visualization
hist_data = pd.DataFrame({'bins': bins[:-1], 'data': counts})

# Display the result
print(hist_data)
