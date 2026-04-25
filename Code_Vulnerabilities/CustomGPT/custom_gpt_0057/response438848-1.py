
import numpy as np

data = np.random.randn(3000000, 50)
# Ensure data is in the right shape
data = data.reshape(300, 10000, 50)

# To verify the shape of the new array
print(f'New shape: {data.shape}')
