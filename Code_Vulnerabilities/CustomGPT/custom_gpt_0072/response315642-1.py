
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 110, 10)

# Count values in each bin
hist, edges = np.histogram(a, bins=bins)

# Prepare data for display
data = {'Bins': edges[:-1], 'Counts': hist}
hist_df = pd.DataFrame(data)

# Display the table
print(hist_df)
