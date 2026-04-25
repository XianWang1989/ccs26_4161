
import copy

class MyClass:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        """Override this method to use a different new."""
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getstate__(self):
        return {'value': self.value}

    def __setstate__(self, state):
        self.value = state['value']

    def __getnewargs_ex__(self):
        return ((), {})  # No args or kwargs needed for this example.

    def __reduce__(self):
        """Reimplement __reduce__ to handle the new arguments."""
        new_args, new_kwargs = self.__getnewargs_ex__()
        state = self.__getstate__()
        return (type(self).kwargs_new,
                (type(self), new_kwargs,) + tuple(new_args),
                state)

    def __deepcopy__(self, memo):
        """Use pickling to implement deepcopy."""
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result

# Example usage
original = MyClass(42)
deep_copied = copy.deepcopy(original)

print(f'Original value: {original.value}')  # Output: Original value: 42
print(f'Deep copied value: {deep_copied.value}')  # Output: Deep copied value: 42

# Modifying copied value
deep_copied.value = 100
print(f'After modification - Original value: {original.value}')  # Original remains unchanged
print(f'After modification - Deep copied value: {deep_copied.value}')  # Output: 100
