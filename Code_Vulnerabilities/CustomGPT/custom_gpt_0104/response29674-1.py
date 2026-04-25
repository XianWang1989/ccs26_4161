
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert the NumPy array to a list for serialization
array_list = array.tolist()

# Serialize using simplejson
serialized_array = json.dumps(array_list)

# Output the serialized array
print(serialized_array)

# To deserialize back to NumPy array
deserialized_array = np.array(json.loads(serialized_array))
print(deserialized_array)
