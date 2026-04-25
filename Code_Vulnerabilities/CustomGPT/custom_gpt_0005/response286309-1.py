
import pickle

class CustomObject:
    def __init__(self, value):
        self.value = value
        self.metadata = {'info': 'example'}

    def __getstate__(self):
        # Should return the state for pickling
        return self.__dict__

    def __setstate__(self, state):
        # Restore state from unpickled data
        self.__dict__.update(state)

    def __reduce__(self):
        # Customize object creation for pickling
        return (type(self).kwargs_new, (self.value,), self.__getstate__())

    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __deepcopy__(self, memo):
        # Use pickle to create a deepcopy
        if id(self) in memo:
            return memo[id(self)]

        # Pickle the object and unpickle to create a new copy
        result = pickle.loads(pickle.dumps(self))
        memo[id(self)] = result
        return result

# Example usage:
original = CustomObject(42)
copy = original.__deepcopy__({})

print(original.value)  # Output: 42
print(copy.value)      # Output: 42

# Modify copy and check that original is unchanged
copy.value = 100
print(original.value)  # Output: 42
print(copy.value)      # Output: 100
