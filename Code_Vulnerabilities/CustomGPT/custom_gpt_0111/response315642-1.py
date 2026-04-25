
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 with a width of 10

# Calculate histogram
hist, _ = np.histogram(a, bins=bins)

# Prepare data for DataFrame
bin_labels = bins[:-1]  # Use the lower edge of bins for labeling
data = {'bins': bin_labels, 'counts': hist}

# Create a DataFrame
hist_df = pd.DataFrame(data)

# Display the result
print(hist_df)
