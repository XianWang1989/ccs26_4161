
import numpy as np

# Simulate your data
data = np.random.randn(3000000, 50)

# Reshape the data 
# Ensure that the total number of elements matches, that is 300 * 10000 * 50 = 3000000 * 50
reshaped_data = data.reshape(300, 10000, 50)

# Verify the shapes
print("Original shape:", data.shape)           # (3000000, 50)
print("Reshaped shape:", reshaped_data.shape)  # (300, 10000, 50)
