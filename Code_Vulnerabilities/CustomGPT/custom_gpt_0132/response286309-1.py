
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
        return (type(self).kwargs_new, (type(self), new_kwargs) + tuple(new_args), state)


class MyClass(MyBase):
    def __init__(self, value):
        self.value = value

    def __deepcopy__(self, memo):
        # Use the reduce method to create a new instance
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result

# Example usage
obj1 = MyClass(42)
obj2 = copy.deepcopy(obj1)

print(f"Original Value: {obj1.value}")  # Output: Original Value: 42
print(f"Copied Value: {obj2.value}")     # Output: Copied Value: 42
