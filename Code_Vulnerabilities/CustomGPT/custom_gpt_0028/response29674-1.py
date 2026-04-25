
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert NumPy array to list for serialization
array_list = array.tolist()

# Serialize using simplejson
serialized_array = json.dumps(array_list)

# Display the serialized array
print(serialized_array)
