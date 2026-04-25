
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Serialize the NumPy array to JSON
array_json = json.dumps(array.tolist())

print("Serialized NumPy array:", array_json)

# Deserialize back to NumPy array
deserialized_array = np.array(json.loads(array_json))

print("Deserialized NumPy array:")
print(deserialized_array)
