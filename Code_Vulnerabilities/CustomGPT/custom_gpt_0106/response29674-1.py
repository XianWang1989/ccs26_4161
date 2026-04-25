
import numpy as np
import simplejson as json

# Create a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Method 1: Convert to list
arr_list = arr.tolist()
serialized_list = json.dumps(arr_list)
print("Serialized with tolist():", serialized_list)

# Method 2: Custom encoder
class NumPyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

serialized_numpy = json.dumps(arr, cls=NumPyEncoder)
print("Serialized with custom encoder:", serialized_numpy)
