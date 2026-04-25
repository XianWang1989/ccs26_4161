
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert the NumPy array to a list
array_list = array.tolist()

# Serialize the list to a JSON formatted string
json_data = json.dumps(array_list)

# Output the serialized JSON string
print(json_data)

# Deserialize back to a NumPy array
deserialized_array = np.array(json.loads(json_data))
print(deserialized_array)
