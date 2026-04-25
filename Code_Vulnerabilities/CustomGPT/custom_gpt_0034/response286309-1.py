
import copy

class MyBaseClass:
    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getstate__(self):
        # Customize the state to be pickled
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__.update(state)

    def __getnewargs_ex__(self):
        return ((), {})

    def __reduce__(self):
        new_args, new_kwargs = self.__getnewargs_ex__()
        state = self.__getstate__()
        return (type(self).kwargs_new, (type(self), new_kwargs) + tuple(new_args), state)


class MyClass(MyBaseClass):
    def __init__(self, value):
        self.value = value

    def __deepcopy__(self, memo, **options):
        if id(self) in memo:
            return memo[id(self)]

        new, args, state = self.__reduce__()
        result = new(*args)

        # Use options to customize copying
        if options.get("copy_value", True):
            result.value = copy.deepcopy(self.value, memo)

        if state:
            result.__setstate__(state)

        memo[id(self)] = result
        return result

# Example usage
original = MyClass([1, 2, 3])
copied = copy.deepcopy(original, copy_value=False)  # Will not copy the 'value' attribute
print(original.value)  # [1, 2, 3]
print(copied.value)    # Still the default value (None or whatever is set during __init__)
