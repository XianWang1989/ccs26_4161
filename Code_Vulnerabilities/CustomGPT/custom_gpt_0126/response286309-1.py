
import copy

class MyBaseClass:
    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

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

class MyClass(MyBaseClass):
    def __init__(self, name):
        self.name = name
        self.data = [1, 2, 3]

    def __deepcopy__(self, memo, options=None):
        if options is None:
            options = {}

        new, args, state = self.__reduce__()
        result = new(*args)

        if state:
            result.__setstate__(state)

        # Example usage of options
        if options.get("copy_data", True):
            result.data = copy.deepcopy(self.data, memo)

        memo[id(self)] = result
        return result

# Example usage
original = MyClass("example")
deep_copied = copy.deepcopy(original, options={"copy_data": True})

print(original.name, original.data)  # Outputs: example [1, 2, 3]
print(deep_copied.name, deep_copied.data)  # Outputs: example [1, 2, 3]
