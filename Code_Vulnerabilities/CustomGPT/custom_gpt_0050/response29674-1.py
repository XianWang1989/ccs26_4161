
import numpy as np
import simplejson as json

# Create a sample NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Serialize the NumPy array by converting it to a list
array_list = array.tolist()
serialized = json.dumps(array_list)

print("Serialized NumPy array:", serialized)

# To deserialize back to a NumPy array
deserialized = json.loads(serialized)
reconstructed_array = np.array(deserialized)

print("Reconstructed NumPy array:\n", reconstructed_array)
