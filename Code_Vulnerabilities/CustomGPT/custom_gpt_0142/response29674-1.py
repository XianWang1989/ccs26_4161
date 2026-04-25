
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert NumPy array to a list
array_list = array.tolist()  # Converts the array to a nested list

# Serialize the list using SimpleJSON
serialized = json.dumps(array_list)

# Print the serialized JSON string
print(serialized)

# To deserialize and convert back to a NumPy array
deserialized = json.loads(serialized)
array_from_json = np.array(deserialized)

# Print the resulting NumPy array
print(array_from_json)
