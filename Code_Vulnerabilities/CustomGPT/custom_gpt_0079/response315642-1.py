
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Specify bins
bins = np.arange(0, 110, 10)

# Compute the histogram
hist, _ = np.histogram(a, bins=bins)

# Create a DataFrame for better formatting
bins_label = [f"{b}" for b in bins[:-1]]  # Exclude the last bin's upper edge
df = pd.DataFrame({'bins': bins_label, 'data': hist})

# Print the DataFrame
print(df.to_string(index=False))
