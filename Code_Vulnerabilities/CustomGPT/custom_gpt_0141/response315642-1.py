
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins (you can adjust the range and size of the bins as needed)
bins = np.arange(0, 110, 10)  # Bins from 0 to 100 with a width of 10

# Create the histogram
hist, edges = np.histogram(a, bins=bins)

# Create a DataFrame for a cleaner output
output = pd.DataFrame({'Bins': edges[:-1], 'Data': hist})

# Display the output
print(output)
