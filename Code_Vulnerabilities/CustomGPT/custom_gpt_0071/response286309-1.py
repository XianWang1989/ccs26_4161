
import copy

class MyClass:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getstate__(self):
        return {"value": self.value}

    def __setstate__(self, state):
        self.value = state["value"]

    def __getnewargs_ex__(self):
        return ((), {})

    def __reduce__(self):
        new_args, new_kwargs = self.__getnewargs_ex__()
        state = self.__getstate__()
        return (type(self).kwargs_new, (type(self), new_kwargs) + tuple(new_args), state)

    def __deepcopy__(self, memo):
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result

# Example usage
original = MyClass(10)
deep_copied = copy.deepcopy(original)

print(original.value)  # Output: 10
print(deep_copied.value)  # Output: 10
deep_copied.value = 20
print(original.value)  # Output: 10 (the original object is unchanged)
