
import numpy as np

# Create a sample data matrix
data = np.random.randn(3000000, 50)

# Reshape the data into shape (300, 10000, 50)
# Note: Ensure that the total number of elements matches
reshaped_data = data.reshape(300, 10000, 50)

print(reshaped_data.shape)  # Should output (300, 10000, 50)
