
import numpy as np

# Generate a sample array
data = np.random.randn(3000000, 50)

# Reshape the data
new_shape = (300, 10000, 50)
reshaped_data = data.reshape(new_shape)

# Verify the shape
print(reshaped_data.shape)  # Should output: (300, 10000, 50)
