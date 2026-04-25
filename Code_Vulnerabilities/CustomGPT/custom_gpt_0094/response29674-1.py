
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert the NumPy array to a list
array_list = array.tolist()

# Serialize the list using simplejson
serialized = json.dumps(array_list)

print("Serialized NumPy array:", serialized)

# To deserialize back to a NumPy array
deserialized = json.loads(serialized)
array_back = np.array(deserialized)

print("Deserialized NumPy array:\n", array_back)
