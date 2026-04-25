
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define bins
bins = np.arange(0, 110, 10)  # Create bins from 0 to 100 with a width of 10
hist, edges = np.histogram(a, bins=bins)

# Prepare data for output
bin_centers = [(edges[i] + edges[i+1]) / 2 for i in range(len(edges) - 1)]
data = {'bins': bin_centers, 'data': hist}

# Convert to DataFrame for better display
df = pd.DataFrame(data)

# Display the Resulting DataFrame
print(df)
