
import numpy as np
import pandas as pd

# Step 1: Input data
a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

# Step 2: Define bins
bins = np.arange(0, 110, 10)  # Bins from 0 to 100 with a width of 10

# Step 3: Calculate histogram
hist, _ = np.histogram(a, bins=bins)

# Step 4: Prepare output DataFrame
bin_centers = bins[:-1] + 5  # Center of each bin
result = pd.DataFrame({'bins': bin_centers, 'data': hist})

# Step 5: Display the result
print(result)
