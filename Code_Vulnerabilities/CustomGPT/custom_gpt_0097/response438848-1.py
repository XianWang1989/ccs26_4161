
import numpy as np

# Create a random matrix of size 3000000x50
data = np.random.randn(3000000, 50)

# Reshape into 300 matrices of size 10000x50
D = data.reshape(300, 10000, 50)

# Check the shape of the new 3D array
print(D.shape)
