
import copy

class MyBaseClass:
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


class MyClass(MyBaseClass):
    def __init__(self, data):
        self.data = data

    def __deepcopy__(self, memo, options=None):
        if options is None:
            options = {}

        new, args, state = self.__reduce__()
        result = new(*args)

        if state:
            result.__setstate__(state)

        memo[id(self)] = result

        # Example: Custom behavior based on options
        if options.get('copy_data', True):
            result.data = copy.deepcopy(self.data, memo)

        return result

# Example usage
if __name__ == "__main__":
    original = MyClass(data=[1, 2, 3])
    options = {'copy_data': True}
    cloned = copy.deepcopy(original, options=options)

    print(original.data)  # Output: [1, 2, 3]
    print(cloned.data)    # Output: [1, 2, 3]

    original.data.append(4)
    print(original.data)  # Output: [1, 2, 3, 4]
    print(cloned.data)    # Output: [1, 2, 3] - remains unchanged
