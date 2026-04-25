
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 with a step of 10

# Calculate the histogram
hist, _ = np.histogram(a, bins=bins)

# Prepare the bin labels
bin_labels = bins[:-1] + 5  # Center of each bin for display

# Create a DataFrame to display in table format
data = {'bins': bin_labels, 'data': hist}
df = pd.DataFrame(data)

# Print the result
print(df)
