
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 110, 10)  # Create bins from 0 to 100 with a width of 10

# Create the histogram
hist, edges = np.histogram(a, bins=bins)

# Prepare the bin labels
bin_labels = [(edges[i], hist[i]) for i in range(len(hist))]

# Convert to DataFrame for easier display
result_df = pd.DataFrame(bin_labels, columns=['Bin Start', 'Count'])

# Display the result
print(result_df)
