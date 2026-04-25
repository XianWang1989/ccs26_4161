
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert the NumPy array to a list
array_list = array.tolist()

# Serialize the list to a JSON string
json_string = json.dumps(array_list)

# Print the JSON string
print(json_string)

# Deserialize back to a NumPy array
deserialized_array = np.array(json.loads(json_string))

# Print the deserialized NumPy array
print(deserialized_array)
