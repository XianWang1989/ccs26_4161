
import numpy as np
import simplejson as json

# Create a sample NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert the NumPy array to a list for serialization
array_list = array.tolist()

# Serialize the list using simplejson
serialized_array = json.dumps(array_list)

# Print the serialized JSON string
print(serialized_array)

# To deserialize back to a NumPy array
deserialized_list = json.loads(serialized_array)
deserialized_array = np.array(deserialized_list)

# Print the deserialized NumPy array
print(deserialized_array)
