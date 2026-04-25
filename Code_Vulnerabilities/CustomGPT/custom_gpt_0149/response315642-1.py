
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 with a width of 10

# Calculate histogram
counts, _ = np.histogram(a, bins=bins)

# Prepare data for output
bin_mids = bins[:-1]  # Get the lower edges of the bins
data = {'bins': bin_mids, 'counts': counts}

# Convert to DataFrame for better formatting
df = pd.DataFrame(data)

# Display the table
print(df)
