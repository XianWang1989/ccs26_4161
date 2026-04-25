
import copy

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
                (type(self), new_kwargs,) + tuple(new_args),
                state)

class CustomClass(BaseClass):
    def __init__(self, name):
        self.name = name
        self.data = []

    def __deepcopy__(self, memo, options=None):
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result

        # Handle custom options here
        if options and 'include_data' in options and options['include_data']:
            result.data = copy.deepcopy(self.data, memo)

        return result

# Example usage
original = CustomClass("Test")
original.data = [1, 2, 3]

# Creating a deepcopy
options = {'include_data': True}
deep_copied = copy.deepcopy(original, memo=None, options=options)

print(deep_copied.name)  # Output: Test
print(deep_copied.data)  # Output: [1, 2, 3]
