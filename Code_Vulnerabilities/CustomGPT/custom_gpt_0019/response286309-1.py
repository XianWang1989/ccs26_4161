
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
    def __init__(self, value):
        self.value = value

    def __deepcopy__(self, memo):
        new, args, state = self.__reduce__()
        result = new(*args)  # Create a new instance
        if state:
            result.__setstate__(state)  # Restore state if needed
        memo[id(self)] = result  # Keep track of copied objects
        return result

# Example usage
if __name__ == "__main__":
    original = MyClass(10)
    copied = copy.deepcopy(original)

    print("Original Value:", original.value)
    print("Copied Value:", copied.value)
