
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert the NumPy array to a list
array_list = array.tolist()

# Serialize the list to a JSON string
json_data = json.dumps(array_list)

# Print the JSON string
print(json_data)

# Deserialize back to a list
deserialized_array = json.loads(json_data)

# Convert back to a NumPy array
new_array = np.array(deserialized_array)

print(new_array)
