
import numpy as np
import simplejson as json

# Create a sample numpy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert the numpy array to a list
array_list = array.tolist()

# Serialize using SimpleJSON
serialized = json.dumps(array_list)

# Output the serialized JSON string
print(serialized)

# To deserialize back to a NumPy array
deserialized = json.loads(serialized)
array_from_json = np.array(deserialized)

# Output the reconstructed NumPy array
print(array_from_json)
