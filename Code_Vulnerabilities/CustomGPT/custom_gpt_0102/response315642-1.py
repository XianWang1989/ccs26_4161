
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 with a width of 10

# Create histogram data
hist, edges = np.histogram(a, bins=bins)

# Prepare the output in table format
data = {'bins': edges[:-1], 'counts': hist}
hist_df = pd.DataFrame(data)

# Display the result
print(hist_df)
