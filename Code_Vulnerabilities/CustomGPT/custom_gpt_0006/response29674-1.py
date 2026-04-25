
import numpy as np
import simplejson as sj

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert the NumPy array to a list for serialization
array_list = array.tolist()

# Serialize the list using simplejson
serialized_array = sj.dumps(array_list)

print(serialized_array)

# To deserialize back to NumPy array
deserialized_array = sj.loads(serialized_array)
array_back = np.array(deserialized_array)

print(array_back)
