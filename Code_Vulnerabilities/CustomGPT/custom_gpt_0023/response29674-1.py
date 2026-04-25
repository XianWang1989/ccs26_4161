
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert the NumPy array to a list for serialization
array_list = array.tolist()

# Serialize the list using SimpleJSON
serialized_data = json.dumps(array_list)

# Output the serialized JSON
print(serialized_data)
