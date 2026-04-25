
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Create bins from 10 to 100
bins = np.arange(10, 101, 10)  # Adjust the range as needed

# Calculate histogram
hist_values, _ = np.histogram(a, bins=bins)

# Prepare the output in table format
output_df = pd.DataFrame({'bins': bins[:-1], 'value': hist_values})

# Display the result
print(output_df)
