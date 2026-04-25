
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bin edges
bins = np.arange(10, 110, 10)  # Creates bins from 10 to 110 (exclusive of 110) with a step size of 10

# Use numpy's histogram function to calculate counts in each bin
counts, _ = np.histogram(a, bins)

# Create a DataFrame for better formatting and display
histogram_data = pd.DataFrame({'Bins': bins[:-1], 'Count': counts})

# Printing the output in the desired format
print(histogram_data.to_string(index=False))
