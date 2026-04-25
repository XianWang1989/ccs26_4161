
import numpy as np
import pandas as pd
from collections import Counter

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 110, 10)

# Count occurrences in each bin
hist, edges = np.histogram(a, bins=bins)

# Prepare data in a table format
bin_labels = [f"{int(edge)}" for edge in edges[:-1]]  # Get bin labels
data = pd.DataFrame({'bins': bin_labels, 'data': hist})

# Output the result
print(data)
