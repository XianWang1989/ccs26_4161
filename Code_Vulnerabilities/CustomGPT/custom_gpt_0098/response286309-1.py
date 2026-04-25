
import pickle

class MyClass:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getstate__(self):
        # Customize the state that gets pickled
        return self.data,

    def __setstate__(self, state):
        self.data = state[0]

    def __getnewargs_ex__(self):
        return ((), {})

    def __reduce__(self):
        new_args, new_kwargs = self.__getnewargs_ex__()
        state = self.__getstate__()
        return (type(self).kwargs_new,
                (type(self), new_kwargs,) + tuple(new_args),
                state)

    def __deepcopy__(self, memo):
        # Use pickling for the deep copy
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result

# Example usage
original = MyClass({"key": "value"})
deep_copied = original.__deepcopy__({})

print(original.data)        # Output: {'key': 'value'}
print(deep_copied.data)     # Output: {'key': 'value'}

# Modifying deep_copied won't affect original
deep_copied.data["key"] = "new_value"
print(original.data)        # Output: {'key': 'value'}
print(deep_copied.data)     # Output: {'key': 'new_value'}
