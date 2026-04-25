
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins (0 to 100 with a step of 10)
bins = np.arange(0, 110, 10)

# Create a histogram
hist, bin_edges = np.histogram(a, bins=bins)

# Create a DataFrame for better visualization
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
hist_df = pd.DataFrame({'bins': bin_centers, 'data': hist})

# Display the result
print(hist_df)
