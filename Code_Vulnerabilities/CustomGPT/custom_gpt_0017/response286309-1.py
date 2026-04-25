
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
        return ((), {'value': self.value})

    def __reduce__(self):
        new_args, new_kwargs = self.__getnewargs_ex__()
        state = self.__getstate__()
        return (type(self).kwargs_new,
                (type(self), new_kwargs,) + tuple(new_args),
                state)

    def __deepcopy__(self, memo, options=None):
        # Example of handling additional options
        if options and options.get('ignore_value'):
            # Skip copying value
            new_instance = type(self).__new__(type(self))
            new_instance.__dict__.update({'value': None})
            memo[id(self)] = new_instance
            return new_instance

        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result

# Example Usage
original = CustomClass(10)
deep_copied = copy.deepcopy(original, memo={})

# With options
options = {'ignore_value': True}
special_copied = copy.deepcopy(original, memo={}, options=options)

print(f'Original value: {original.value}')  # Output: 10
print(f'Deep copied value: {deep_copied.value}')  # Output: 10
print(f'Special copied value: {special_copied.value}')  # Output: None
