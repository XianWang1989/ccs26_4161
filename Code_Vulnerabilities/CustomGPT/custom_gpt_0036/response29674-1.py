
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert the NumPy array to a list
array_list = array.tolist()

# Serialize the list using simplejson
serialized_array = json.dumps(array_list)

# Print the serialized output
print("Serialized NumPy Array:", serialized_array)

# To deserialize the array back to a NumPy array
deserialized_array = np.array(json.loads(serialized_array))

# Print the deserialized NumPy array
print("Deserialized NumPy Array:\n", deserialized_array)
