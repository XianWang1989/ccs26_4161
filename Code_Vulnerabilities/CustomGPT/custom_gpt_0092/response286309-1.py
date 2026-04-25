
import copy
import pickle

class BaseClass:
    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getstate__(self):
        return {}

    def __setstate__(self, state):
        self.__dict__.update(state)

    def __getnewargs_ex__(self):
        return ((), {})

    def __reduce__(self):
        new_args, new_kwargs = self.__getnewargs_ex__()
        state = self.__getstate__()
        return (type(self).kwargs_new,
                (type(self), new_kwargs) + tuple(new_args),
                state)

class CustomClass(BaseClass):
    def __init__(self, data):
        self.data = data

    def __deepcopy__(self, memo):
        # Use pickle to make a deepcopy
        if id(self) in memo:
            return memo[id(self)]

        # Pickle the object to serialize
        pickled_obj = pickle.dumps(self)
        # Unpickle to create a new object
        new_obj = pickle.loads(pickled_obj)

        # Register the memoization
        memo[id(self)] = new_obj
        return new_obj

# Example usage
original = CustomClass([1, 2, 3])
deep_copied = copy.deepcopy(original)

# Verify the copying
print(original.data)         # Output: [1, 2, 3]
print(deep_copied.data)     # Output: [1, 2, 3]
print(original is deep_copied)  # Output: False
