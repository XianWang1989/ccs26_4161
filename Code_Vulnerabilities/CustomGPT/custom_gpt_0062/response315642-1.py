
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 101, 10)  # Bins from 0 to 100 with a width of 10

# Create a histogram
hist, edges = np.histogram(a, bins=bins)

# Prepare the data for the DataFrame
bin_centers = [(edges[i] + edges[i + 1]) / 2 for i in range(len(edges) - 1)]
data = {'bins': bin_centers, 'counts': hist}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
