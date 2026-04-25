
import numpy as np

# Generate random data
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array
# 3000000 rows divided into 300 segments of 10000 rows each and 50 columns
data_reshaped = data.reshape(300, 10000, 50)

# Check the shape of the new 3D array
print(data_reshaped.shape)  # Should output: (300, 10000, 50)
