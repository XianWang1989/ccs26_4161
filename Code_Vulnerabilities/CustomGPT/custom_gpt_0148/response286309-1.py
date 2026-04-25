
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


class Example(Base):
    def __init__(self, value):
        self.value = value

    def __deepcopy__(self, memo):
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result


# Example usage
if __name__ == "__main__":
    obj1 = Example(42)

    # Performing a deep copy
    obj2 = copy.deepcopy(obj1)

    print("Original:", obj1.value)  # Output: Original: 42
    print("Copied:", obj2.value)     # Output: Copied: 42

    # Modifying the copied object's value
    obj2.value = 100
    print("After modification:")
    print("Original:", obj1.value)  # Output: Original: 42
    print("Copied:", obj2.value)     # Output: Copied: 100
