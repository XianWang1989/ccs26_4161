
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert the NumPy array to a list for serialization
array_list = array.tolist()

# Serialize using SimpleJSON
serialized_array = json.dumps(array_list)

# Print the serialized JSON string
print(serialized_array)
