
import numpy as np
import simplejson as json

# Create a sample NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Serialize using SimpleJSON
array_json = json.dumps(array.tolist())

print(array_json)
