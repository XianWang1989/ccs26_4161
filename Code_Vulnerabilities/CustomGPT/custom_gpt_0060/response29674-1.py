
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert NumPy array to a list
array_list = array.tolist()

# Serialize the list using simplejson
serialized_data = json.dumps(array_list)

# Print the serialized JSON string
print(serialized_data)

# To deserialize it back into a NumPy array
deserialized_data = json.loads(serialized_data)
array_back = np.array(deserialized_data)

# Print the deserialized NumPy array
print(array_back)
