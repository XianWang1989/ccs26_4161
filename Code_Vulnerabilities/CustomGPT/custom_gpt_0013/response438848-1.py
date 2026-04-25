
import numpy as np

# Generate random data
data = np.random.randn(3000000, 50)

# Reshape the data into the desired shape
# The first dimension is the number of windows (300),
# The second dimension is the length of each window (10000),
# The third dimension corresponds to the columns (50)
reshaped_data = data.reshape(300, 10000, 50)

# Check the shape to confirm
print(reshaped_data.shape)  # Output should be (300, 10000, 50)
