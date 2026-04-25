
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(10, 110, 10)  # Bins from 10 to 100 with width 10

# Create a histogram
hist, bin_edges = np.histogram(a, bins=bins)

# Prepare the bin data in the desired format
bin_data = {'bins': bin_edges[:-1], 'data': hist}

# Convert to DataFrame for pretty printing
df = pd.DataFrame(bin_data)

# Print the result in table format
print(df)

# Optional: Format the output to your specific needs
for index, row in df.iterrows():
    print(f"{int(row['bins'])}  {row['data']}")
