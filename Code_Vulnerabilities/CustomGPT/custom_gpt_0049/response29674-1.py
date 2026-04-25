
import numpy as np
import simplejson as json

# Create a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Serialize the NumPy array to JSON
json_data = json.dumps(arr.tolist())

# Deserialize back to NumPy array
loaded_arr = np.array(json.loads(json_data))

print("Serialized JSON:", json_data)
print("Deserialized NumPy Array:\n", loaded_arr)
