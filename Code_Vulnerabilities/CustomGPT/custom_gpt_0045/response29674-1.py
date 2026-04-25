
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert NumPy array to a list for serialization
array_list = array.tolist()

# Serialize the list using simplejson
serialized_array = json.dumps(array_list)

print("Serialized NumPy array:", serialized_array)

# To deserialize back to a NumPy array
deserialized_array = np.array(json.loads(serialized_array))
print("Deserialized NumPy array:\n", deserialized_array)
