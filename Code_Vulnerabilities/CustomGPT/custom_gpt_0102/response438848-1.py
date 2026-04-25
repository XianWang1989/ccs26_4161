
import numpy as np

# Generate random data
data = np.random.randn(3000000, 50)

# Reshape the data:
# Shape it into (300, 10000, 50)
reshaped_data = data.reshape(300, 10000, 50)

# Verify the shape
print("New shape:", reshaped_data.shape)
