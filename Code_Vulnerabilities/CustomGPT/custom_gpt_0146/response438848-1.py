
import numpy as np

# Create a sample matrix of size (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape data into (300, 10000, 50)
D_reshaped = data.reshape((300, 10000, 50))

print("Shape of the original data: ", data.shape)
print("Shape of the reshaped data: ", D_reshaped.shape)
