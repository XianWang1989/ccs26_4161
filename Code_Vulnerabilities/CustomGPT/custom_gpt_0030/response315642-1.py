
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 with a width of 10

# Calculate the histogram
hist, edges = np.histogram(a, bins=bins)

# Create a DataFrame for better visualization
bin_centers = (edges[:-1] + edges[1:]) / 2  # Calculate the centers of each bin
data = {'bins': bin_centers.astype(int), 'count': hist}
df = pd.DataFrame(data)

# Display the result
print(df)
