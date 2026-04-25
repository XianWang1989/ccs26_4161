
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 101, 10)

# Calculate the histogram
hist, edges = np.histogram(a, bins=bins)

# Create a DataFrame for better formatting
bin_labels = [f"{edges[i]} - {edges[i+1]}" for i in range(len(edges) - 1)]
data = {'bins': edges[:-1], 'count': hist}

# Convert to DataFrame
df = pd.DataFrame(data)

# Print the result
print(df)
