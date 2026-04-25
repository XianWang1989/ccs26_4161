
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 with a width of 10

# Create histogram data
hist, _ = np.histogram(a, bins)

# Create a DataFrame for better formatting
bin_labels = bins[:-1]  # Use the left edge of bins as labels
data = pd.DataFrame({'bins': bin_labels, 'data': hist})

# Display the table
print(data)
