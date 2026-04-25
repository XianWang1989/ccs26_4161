
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Serialize the array by converting it to a list
array_list = array.tolist()
serialized_array = json.dumps(array_list)

print(serialized_array)

# To deserialize back to a NumPy array
deserialized_array = np.array(json.loads(serialized_array))
print(deserialized_array)
