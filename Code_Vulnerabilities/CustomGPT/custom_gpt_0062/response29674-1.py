
import numpy as np
import simplejson as json

# Create a sample NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Function to serialize NumPy array
def serialize_numpy_array(arr):
    return json.dumps(arr.tolist())  # Convert to list and then serialize

# Serialize the array
serialized_array = serialize_numpy_array(array)

print("Serialized NumPy array:", serialized_array)

# To deserialize back to a NumPy array
deserialized_array = np.array(json.loads(serialized_array))
print("Deserialized NumPy array:\n", deserialized_array)
