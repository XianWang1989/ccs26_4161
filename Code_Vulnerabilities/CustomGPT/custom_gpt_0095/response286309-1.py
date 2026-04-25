
import copy

class MyBase:
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


class MyClass(MyBase):
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def __deepcopy__(self, memo, options=None):
        new, args, state = self.__reduce__()
        result = new(*args)

        if options is not None and 'ignore_names' in options:
            for name in options['ignore_names']:
                if name in self.__dict__:
                    delattr(result, name)

        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result


# Example usage
original = MyClass("Example", [1, 2, 3])
options = {'ignore_names': ['data']}
deep_copied = copy.deepcopy(original, memo={})

print(original.__dict__)  # Output: {'name': 'Example', 'data': [1, 2, 3]}
print(deep_copied.__dict__)  # Output will depend on `options`
