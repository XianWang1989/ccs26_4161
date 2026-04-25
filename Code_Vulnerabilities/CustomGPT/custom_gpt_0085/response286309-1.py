
import copy
import pickle

class MyBaseClass:
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
                (type(self), new_kwargs,) + tuple(new_args),
                state)

class MyClass(MyBaseClass):
    def __init__(self, data):
        self.data = data

    def __deepcopy__(self, memo):
        # Use pickle to create a deepcopy
        new_instance = pickle.loads(pickle.dumps(self, protocol=pickle.HIGHEST_PROTOCOL))

        # Optionally modify the new instance according to additional options
        # For example, you could ignore certain attributes based on a condition
        memo[id(self)] = new_instance
        return new_instance

# Example Usage
original = MyClass({"key": "value"})
deep_copied = copy.deepcopy(original)

print("Original:", original.data)  # Output: {'key': 'value'}
print("Deep Copied:", deep_copied.data)  # Output: {'key': 'value'}
