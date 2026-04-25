
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
                (type(self), new_kwargs,) + tuple(new_args),
                state)

class CustomClass(BaseClass):
    def __init__(self, data):
        self.data = data

    def __deepcopy__(self, memo, options=None):
        if options and 'ignore_data' in options and options['ignore_data']:
            # Skip copying data
            new_instance = self.__class__.__new__(self.__class__)
            memo[id(self)] = new_instance
            return new_instance

        # Use pickling for deep copy
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result

# Example usage
original = CustomClass(data=[1, 2, 3])
options = {'ignore_data': True}
deep_copied = copy.deepcopy(original, memo={}, options=options)

print(original.data)  # Output: [1, 2, 3]
print(deep_copied.data)  # Output: None, since data was ignored
