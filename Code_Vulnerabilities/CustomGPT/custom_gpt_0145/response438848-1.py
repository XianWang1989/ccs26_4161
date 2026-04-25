
import numpy as np

# Generate random data
data = np.random.randn(3000000, 50)

# You want to reshape it into 300 matrices of size 10000x50
# Ensure the total size matches
if data.shape[0] != 3000000 or data.shape[1] != 50:
    raise ValueError("Input data must be of size 3000000x50")

# Reshape the data
reshaped_data = data.reshape(300, 10000, 50)

# Optional: Verify the shape of the reshaped data
print(reshaped_data.shape)  # Output should be (300, 10000, 50)
