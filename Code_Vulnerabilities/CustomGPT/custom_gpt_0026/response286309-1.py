
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
                (type(self), new_kwargs,) + tuple(new_args),
                state)

class MyClass(Base):
    def __init__(self, data):
        self.data = data

    def __deepcopy__(self, memo, options=None):
        if options is None:
            options = {}

        # Pickling method for deepcopy
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)

        # Example of using options
        if options.get("copy_data", True):
            result.data = copy.deepcopy(self.data, memo)

        memo[id(self)] = result
        return result

# Example usage
original = MyClass([1, 2, 3])
options = {"copy_data": False}
deep_copied = copy.deepcopy(original, options=options)

print(original.data)  # Output: [1, 2, 3]
print(deep_copied.data)  # Output: [1, 2, 3] (if copy_data is True)
