
import numpy as np
import pandas as pd

# Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Define the bins
bins = np.arange(10, 110, 10)

# Create the histogram
hist, edges = np.histogram(a, bins=bins)

# Create a DataFrame for better formatting
data = {'Bins': bins[:-1], 'Counts': hist}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Optionally, to format the output as required:
for index, row in df.iterrows():
    print(f"{row['Bins']}  {row['Counts']}")
