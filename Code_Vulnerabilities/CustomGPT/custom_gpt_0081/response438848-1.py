
import numpy as np

# Generating a random matrix of size (3000000, 50)
data = np.random.randn(3000000, 50)

# Reshape the data into shape (300, 10000, 50)
data_reshaped = data.reshape(300, 10000, 50)

print("Original shape:", data.shape)
print("New shape:", data_reshaped.shape)
