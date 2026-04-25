
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert to list and serialize
serialized_array = json.dumps(array.tolist())

print(serialized_array)
