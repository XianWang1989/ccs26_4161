
import copy

class CustomBase:
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

class MyClass(CustomBase):
    def __init__(self, data):
        self.data = data

    def __deepcopy__(self, memo, options=None):
        # Custom behavior based on options
        if options and options.get("copy_data", True):
            new, args, state = self.__reduce__()
            result = new(*args)
            result.__setstate__(state)
            result.data = copy.deepcopy(self.data, memo)
        else:
            result = MyClass(None)  # or some other default behavior

        memo[id(self)] = result
        return result

# Usage Example
if __name__ == "__main__":
    original = MyClass({'key': 'value'})
    # Default deepcopy
    copied = copy.deepcopy(original)
    print(copied.data)  # Output: {'key': 'value'}

    # Custom deepcopy with options
    options = {'copy_data': False}
    partial_copy = copy.deepcopy(original, memo={}, options=options)
    print(partial_copy.data)  # Output: None
