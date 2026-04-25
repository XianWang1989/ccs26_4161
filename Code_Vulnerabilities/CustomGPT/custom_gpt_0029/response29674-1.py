
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert the NumPy array to a list
array_list = array.tolist()

# Serialize using SimpleJSON
serialized = json.dumps(array_list)

# Print the serialized JSON string
print(serialized)

# To deserialize back to a NumPy array
deserialized = json.loads(serialized)
array_deserialized = np.array(deserialized)

# Print the deserialized NumPy array
print(array_deserialized)
