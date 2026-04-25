
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins (you can adjust the range and intervals as needed)
bins = np.arange(0, 101, 10)  # This creates bins from 0 to 100 with step 10

# Use np.histogram to compute the histogram
hist, bin_edges = np.histogram(a, bins=bins)

# Create a DataFrame to display bins and their corresponding counts
histogram_data = pd.DataFrame({
    'bins': bin_edges[:-1],  # lower edges of bins
    'data': hist              # counts in each bin
})

# Print the resulting DataFrame
print(histogram_data)
