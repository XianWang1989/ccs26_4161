
import copy

class MyClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        """
        Override this method to use a different new.
        """
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getstate__(self):
        # Return the state for pickling
        return (self.attribute1, self.attribute2)

    def __setstate__(self, state):
        # Restore the state from the unpickled data
        self.attribute1, self.attribute2 = state

    def __getnewargs_ex__(self):
        return ((), {})

    def __reduce__(self):
        new_args, new_kwargs = self.__getnewargs_ex__()
        state = self.__getstate__()
        return (type(self).kwargs_new, (type(self), {},) + new_args, state)

    def __deepcopy__(self, memo):
        # Use pickling for deepcopy
        new, args, state = self.__reduce__()
        result = new(*args)  # Create a new instance
        if state:
            result.__setstate__(state)  # Restore state
        memo[id(self)] = result  # Store in memo
        return result

# Example usage:
original = MyClass("Value1", "Value2")
deep_copied = copy.deepcopy(original)

print(f"Original: {original.attribute1}, {original.attribute2}")
print(f"Deep Copied: {deep_copied.attribute1}, {deep_copied.attribute2}")
