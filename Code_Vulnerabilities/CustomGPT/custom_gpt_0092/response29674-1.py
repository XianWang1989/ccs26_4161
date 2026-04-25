
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert the NumPy array to a list
array_list = array.tolist()

# Serialize the list using simplejson
serialized_data = json.dumps(array_list)

# Print the serialized data
print(serialized_data)

# To deserialize back to a NumPy array
deserialized_data = json.loads(serialized_data)
array_from_json = np.array(deserialized_data)

print(array_from_json)
