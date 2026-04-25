
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Create bins
bins = np.arange(0, 101, 10)

# Create histogram
hist, edges = np.histogram(a, bins=bins)

# Prepare table data
table_data = {str(edge): count for edge, count in zip(edges[:-1], hist)}

# Convert to DataFrame for better visualization
df = pd.DataFrame(list(table_data.items()), columns=['Bins', 'Count'])
print(df)
