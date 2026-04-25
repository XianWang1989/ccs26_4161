
import copy

class CustomClass:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getstate__(self):
        return {'value': self.value}

    def __setstate__(self, state):
        self.value = state['value']

    def __getnewargs_ex__(self):
        return ((), {})

    def __reduce__(self):
        new_args, new_kwargs = self.__getnewargs_ex__()
        state = self.__getstate__()
        return (type(self).kwargs_new, (type(self), new_kwargs) + tuple(new_args), state)

    def __deepcopy__(self, memo, options=None):
        # Handle custom options if any
        if options and 'skip_value' in options and options['skip_value']:
            result = type(self).__new__(type(self))
            memo[id(self)] = result
            return result

        # Default deepcopy behavior
        new, args, state = self.__reduce__()
        result = new(*args)
        result.__setstate__(state)
        memo[id(self)] = result
        return result

# Example Usage
original = CustomClass(10)
memo = {}
print(f'Original Value: {original.value}')  # Output: Original Value: 10

# Perform a deepcopy without options
copied = copy.deepcopy(original, memo)
print(f'Copied Value: {copied.value}')  # Output: Copied Value: 10

# Perform a deepcopy skipping the value
copied_skipped = copy.deepcopy(original, memo, options={'skip_value': True})
print(f'Copied Skipped Value: {copied_skipped.value}')  # Output: Copied Skipped Value: None
