
import copy

class Base:
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
                (type(self), new_kwargs) + tuple(new_args),
                state)

class MyObject(Base):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __deepcopy__(self, memo):
        new, args, state = self.__reduce__()
        result = new(*args)  # Create a new instance using the kwargs_new method
        if state:
            result.__setstate__(state)  # Restore the state if it exists
        memo[id(self)] = result
        return result

# Example usage
original = MyObject(name='example', value=42)
deep_copied = copy.deepcopy(original)

# Verify deep copy
print(deep_copied.name)  # Output: example
print(deep_copied.value)  # Output: 42
print(original is deep_copied)  # Output: False
