
import numpy as np

# Create a random 2D array of size 3000000x50
data = np.random.randn(3000000, 50)

# Reshape the data into a 3D array of shape (300, 10000, 50)
# Note: Ensure that the total number of elements is consistent (300*10000*50 = 15000000)
# Also, we can directly use the reshape function to achieve this
reshaped_data = data.reshape(300, 10000, 50)

# Display the shape of the new 3D array
print(reshaped_data.shape)  # Output should be (300, 10000, 50)
