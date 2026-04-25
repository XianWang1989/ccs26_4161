
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert the NumPy array to a list for serialization
array_list = array.tolist()

# Serialize the list using simplejson
serialized_data = json.dumps(array_list)

# Output the serialized JSON string
print(serialized_data)

# To deserialize back to NumPy array
deserialized_data = json.loads(serialized_data)
array_from_json = np.array(deserialized_data)

# Output the deserialized NumPy array
print(array_from_json)
