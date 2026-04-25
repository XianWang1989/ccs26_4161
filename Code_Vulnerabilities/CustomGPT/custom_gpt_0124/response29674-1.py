
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert to list for serialization
array_list = array.tolist()

# Serialize using SimpleJSON
json_string = json.dumps(array_list)

print(json_string)
