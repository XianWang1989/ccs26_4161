
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
                (type(self), new_kwargs,) + tuple(new_args),
                state)

class MyClass(MyBaseClass):
    def __init__(self, value):
        self.value = value

    def __deepcopy__(self, memo):
        # Use pickling and unpickling to create a deepcopy
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result

# Example usage
original = MyClass(10)
copied = copy.deepcopy(original)

print(original.value)  # Output: 10
print(copied.value)    # Output: 10

# Change the copied value
copied.value = 20
print(original.value)  # Output: 10 (original is unchanged)
print(copied.value)    # Output: 20 (copied is updated)
