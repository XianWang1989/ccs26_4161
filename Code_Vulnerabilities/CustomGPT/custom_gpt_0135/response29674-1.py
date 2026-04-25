
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert the NumPy array to a list
array_list = array.tolist()

# Serialize using simplejson
serialized_data = json.dumps(array_list)

print("Serialized Data:", serialized_data)

# To deserialize back to a NumPy array
deserialized_data = json.loads(serialized_data)
restored_array = np.array(deserialized_data)

print("Restored Array:\n", restored_array)
