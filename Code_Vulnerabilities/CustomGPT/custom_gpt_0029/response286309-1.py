
import copy

class MyClass:
    def __init__(self, value):
        self.value = value

    # Modify __getstate__ to customize what gets pickled
    def __getstate__(self):
        return (self.value,)

    # Modify __setstate__ to customize how to restore the state
    def __setstate__(self, state):
        self.value = state[0]

    def __reduce__(self):
        return (type(self).kwargs_new, (type(self),), self.__getstate__())

    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        # Create a new instance
        instance = cls.__new__(cls, *new_args, **new_kwargs)
        instance.__init__(*new_args, **new_kwargs)
        return instance

    def __deepcopy__(self, memo, options=None):
        if options is not None and 'custom_option' in options:
            # Implement custom behavior based on options
            new_value = options['custom_option'](self.value)
        else:
            new_value = copy.deepcopy(self.value, memo)  # Default deep copy
        result = self.__class__(new_value)
        memo[id(self)] = result
        return result

# Example usage
original = MyClass(10)

# Example function to modify the value during copying
def modify_value(val):
    return val + 5

# Using deepcopy with custom options
options = {'custom_option': modify_value}
copied = copy.deepcopy(original, options=options)

print(original.value)  # Output: 10
print(copied.value)    # Output: 15
