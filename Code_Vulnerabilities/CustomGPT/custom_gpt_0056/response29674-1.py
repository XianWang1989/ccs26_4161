
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert NumPy array to a list
array_list = array.tolist()

# Serialize the list using SimpleJSON
serialized_array = json.dumps(array_list)

# Print the serialized JSON string
print(serialized_array)

# To deserialize back to a NumPy array
deserialized_list = json.loads(serialized_array)
array_from_json = np.array(deserialized_list)

# Print the reconstructed NumPy array
print(array_from_json)
