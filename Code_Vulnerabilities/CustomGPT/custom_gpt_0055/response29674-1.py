
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert NumPy array to a list
array_list = array.tolist()

# Serialize the list using simplejson
serialized_data = json.dumps(array_list)

# Print the serialized JSON
print(serialized_data)

# To deserialize back to a NumPy array
deserialized_data = json.loads(serialized_data)
reconstructed_array = np.array(deserialized_data)

# Print the reconstructed array
print(reconstructed_array)
