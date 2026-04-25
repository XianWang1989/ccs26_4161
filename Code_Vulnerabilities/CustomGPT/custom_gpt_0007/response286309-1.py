
import copy

class BaseClass:
    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        """Override this method to use a different new."""
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

class CustomClass(BaseClass):
    def __init__(self, data):
        self.data = data

    def __deepcopy__(self, memo, options=None):
        if options is None:
            options = {}

        new, args, state = self.__reduce__()
        result = new(*args)

        # Handle additional options if provided
        if options.get('copy_data', True):
            result.data = copy.deepcopy(self.data, memo)

        if state:
            result.__setstate__(state)

        memo[id(self)] = result
        return result

# Example usage
original = CustomClass(data=[1, 2, 3])
deep_copied = copy.deepcopy(original, options={'copy_data': True})

print(original.data)  # Output: [1, 2, 3]
print(deep_copied.data)  # Output: [1, 2, 3]

# Modifying the deep copied instance's data does not affect the original
deep_copied.data.append(4)
print(original.data)  # Output: [1, 2, 3]
print(deep_copied.data)  # Output: [1, 2, 3, 4]
