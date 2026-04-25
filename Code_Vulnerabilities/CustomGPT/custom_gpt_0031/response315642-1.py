
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 with a step of 10

# Compute histogram
hist, _ = np.histogram(a, bins=bins)

# Create a DataFrame for better visualization
bin_edges = bins[:-1]  # Get the left edges of the bins
bin_counts = hist       # Histogram counts
data_dict = {'bins': bin_edges, 'counts': bin_counts}
df = pd.DataFrame(data_dict)

# Display the result
print(df)
