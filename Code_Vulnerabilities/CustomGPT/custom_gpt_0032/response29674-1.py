
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Serialize the NumPy array to a JSON string
json_string = json.dumps(array.tolist())

print(json_string)

# To deserialize back to a NumPy array
array_from_json = np.array(json.loads(json_string))

print(array_from_json)
