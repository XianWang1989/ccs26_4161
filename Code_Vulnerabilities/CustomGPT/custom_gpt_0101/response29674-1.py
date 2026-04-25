
import numpy as np
import simplejson as json

# Create a numpy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Serialize the numpy array using simplejson
serialized_array = json.dumps(array.tolist())

print(serialized_array)
