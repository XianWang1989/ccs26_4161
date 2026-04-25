
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Create bins
bins = np.arange(0, 101, 10)

# Generate histogram data
hist, edges = np.histogram(a, bins=bins)

# Prepare the output in table format
bin_data = pd.DataFrame({'Bins': edges[:-1] + 10, 'Count': hist})

# Display the result
print(bin_data)
