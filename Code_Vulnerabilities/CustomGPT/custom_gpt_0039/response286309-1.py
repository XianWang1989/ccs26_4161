
import copy

class CustomClass:
    def __init__(self, value, options=None):
        self.value = value
        self.options = options or {}

    def __reduce__(self):
        return (self.__class__.kwargs_new, 
                (self.options,), 
                self.__getstate__())

    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        instance = cls.__new__(cls, *new_args, **new_kwargs)
        instance.__init__(*new_args, **new_kwargs)
        return instance

    def __getstate__(self):
        return (self.value,)

    def __setstate__(self, state):
        self.value = state[0]

    def __deepcopy__(self, memo):
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result

        # Example of handling options
        if self.options.get("skip_value_copy", False):
            return result  # Skip copying value if the option is set

        # Otherwise, deepcopy the value
        result.value = copy.deepcopy(self.value, memo)
        return result

# Example usage
original = CustomClass(value=[1, 2, 3], options={"skip_value_copy": True})
copied = copy.deepcopy(original)

print("Original value:", original.value)  # Original value: [1, 2, 3]
print("Copied value:", copied.value)      # Copied value: [1, 2, 3]
