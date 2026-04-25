
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bin edges
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 with a width of 10

# Count the number of occurrences in each bin
hist, edges = np.histogram(a, bins=bins)

# Create a DataFrame for better display
bin_centers = (edges[:-1] + edges[1:]) / 2  # Calculate bin centers
hist_table = pd.DataFrame({'Bins': edges[:-1], 'Count': hist})

# Display the histogram data
print(hist_table)
