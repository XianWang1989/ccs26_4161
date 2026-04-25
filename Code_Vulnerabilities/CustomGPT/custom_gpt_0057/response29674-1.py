
import numpy as np
import simplejson as json

def serialize_numpy_array(array):
    array_list = array.tolist()
    json_data = json.dumps(array_list)
    return json_data

def deserialize_numpy_array(json_data):
    array_list = json.loads(json_data)
    return np.array(array_list)

# Example usage
numpy_array = np.array([[1, 2, 3], [4, 5, 6]])
serialized = serialize_numpy_array(numpy_array)
print("Serialized JSON:", serialized)

deserialized = deserialize_numpy_array(serialized)
print("Deserialized NumPy Array:\n", deserialized)
