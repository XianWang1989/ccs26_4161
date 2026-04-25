
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(10, 110, 10)  # Bins from 10 to 100, inclusive

# Create histogram data
hist, _ = np.histogram(a, bins=bins)

# Create a DataFrame for better formatting
hist_df = pd.DataFrame({'bins': bins[:-1], 'count': hist})

# Displaying the output in the desired format
for index, row in hist_df.iterrows():
    print(f"{row['bins']}  {row['count']}")
