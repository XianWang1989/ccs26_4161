
import copy

class CustomClass:
    # Static method for customized object creation
    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    # State management methods
    def __getstate__(self):
        return self.__dict__

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

    # Custom deepcopy implementation
    def __deepcopy__(self, memo):
        new, args, state = self.__reduce__()
        result = new(*args)  # Create a new instance
        if state:
            result.__setstate__(state)  # Restore state
        memo[id(self)] = result  # Save to memo
        return result

# Example Usage
original = CustomClass()
original.example_attribute = [1, 2, 3]

# Perform deepcopy
deep_copied = copy.deepcopy(original)

print(deep_copied.example_attribute)  # Output: [1, 2, 3]
