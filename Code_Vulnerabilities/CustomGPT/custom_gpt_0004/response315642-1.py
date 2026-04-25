
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(0, 110, 10)  # Bins from 0 to 100 with a step of 10

# Calculate histogram
hist, edges = np.histogram(a, bins=bins)

# Prepare the output data in a DataFrame
data = {'bins': edges[:-1], 'counts': hist}
df = pd.DataFrame(data)

# Display the output
print(df)
