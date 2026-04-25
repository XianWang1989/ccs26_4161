
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Calculate the histogram
hist, edges = np.histogram(a, bins=bins)

# Prepare the output in a DataFrame format
bin_labels = [f"{edges[i]} - {edges[i+1]}" for i in range(len(edges)-1)]
hist_df = pd.DataFrame({'bins': bin_labels, 'data': hist})

# Print the result in the specified format
for index, row in hist_df.iterrows():
    print(f"{row['bins']}  {row['data']}")
