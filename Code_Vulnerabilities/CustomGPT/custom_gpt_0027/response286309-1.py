
import copy

class MyClass:
    def __init__(self, data):
        self.data = data

    def __getstate__(self):
        return {'data': self.data}

    def __setstate__(self, state):
        self.data = state['data']

    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getnewargs_ex__(self):
        return ((), {'data': self.data})

    def __reduce__(self):
        new_args, new_kwargs = self.__getnewargs_ex__()
        state = self.__getstate__()
        return (type(self).kwargs_new, (type(self), new_kwargs) + tuple(new_args), state)

    def __deepcopy__(self, memo, options=None):
        # If options are provided, modify the copying behavior as needed
        if options and 'skip_data' in options and options['skip_data']:
            return MyClass(None)

        new, args, state = self.__reduce__()
        result = new(*args)

        if state:
            result.__setstate__(state)

        memo[id(self)] = result
        return result

# Example usage
original = MyClass([1, 2, 3])
copied = copy.deepcopy(original)  # Regular deepcopy
partially_copied = copy.deepcopy(original, options={'skip_data': True})  # Skip data

print("Original:", original.data)  # Output: [1, 2, 3]
print("Copied:", copied.data)  # Output: [1, 2, 3]
print("Partially Copied:", partially_copied.data)  # Output: None
