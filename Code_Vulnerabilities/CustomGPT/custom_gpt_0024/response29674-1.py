
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([1, 2, 3, 4, 5])

# Serialize the NumPy array to JSON
array_json = json.dumps(array.tolist())

# Print the serialized JSON string
print(array_json)

# To deserialize back to a NumPy array
deserialized_array = np.array(json.loads(array_json))
print(deserialized_array)
