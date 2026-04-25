
import numpy as np

# Generate a sample matrix of size 3000000 x 50
data = np.random.randn(3000000, 50)

# Reshape the data into 300 matrices of size 10000 x 50
reshaped_data = data.reshape(300, 10000, 50)

# Print the shape to verify
print(reshaped_data.shape)  # Output should be (300, 10000, 50)
