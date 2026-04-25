
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Serialize the NumPy array to JSON
json_data = json.dumps(array.tolist())

# Output the serialized JSON
print(json_data)

# To deserialize back to a NumPy array
deserialized_array = np.array(json.loads(json_data))
print(deserialized_array)
