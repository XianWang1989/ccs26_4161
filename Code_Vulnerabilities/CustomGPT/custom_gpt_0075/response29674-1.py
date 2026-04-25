
import numpy as np
import simplejson as json

# Function to serialize a NumPy array
def serialize_numpy_array(array):
    # Use the tolist method for serialization
    return json.dumps(array.tolist())

# Example usage
arr = np.array([[1, 2, 3], [4, 5, 6]])
serialized_arr = serialize_numpy_array(arr)

print(serialized_arr)
