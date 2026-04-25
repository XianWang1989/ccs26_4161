
import numpy as np

# Create a random 2D array
data = np.random.randn(3000000, 50)

# Reshape the array
new_shape = (300, 10000, 50)
reshaped_data = data.reshape(new_shape)

# Check the shape of the new array
print(reshaped_data.shape)  # Should print (300, 10000, 50)
