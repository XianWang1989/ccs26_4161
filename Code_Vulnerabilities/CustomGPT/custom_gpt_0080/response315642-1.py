
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(10, 110, 10)  # Bins from 10 to 100 with a width of 10

# Calculate histogram
hist, _ = np.histogram(a, bins=bins)

# Create a DataFrame for better representation
bin_centers = bins[:-1]  # Centers of the bins
hist_df = pd.DataFrame({'bins': bin_centers, 'data': hist})

# Print the DataFrame
print(hist_df.to_string(index=False))
