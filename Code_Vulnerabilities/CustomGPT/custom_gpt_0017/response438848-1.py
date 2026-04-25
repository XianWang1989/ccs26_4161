
import numpy as np

# Generate synthetic data
data = np.random.randn(3000000, 50)

# Reshape the data into the desired 3D shape
# (300, 10000, 50)
data_reshaped = data.reshape(300, 10000, 50)

# Verify the shape
print(data_reshaped.shape)  # Should output: (300, 10000, 50)
