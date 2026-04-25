
import numpy as np
import simplejson as json

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Convert to list and serialize using SimpleJSON
array_list = array.tolist()
serialized = json.dumps(array_list)

print(serialized)
