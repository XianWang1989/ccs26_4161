
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
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __deepcopy__(self, memo):
        # Use pickling to do the deep copy
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result


# Example usage
original = MyClass("example", [1, 2, 3])
cloned = copy.deepcopy(original)

# Modify the cloned object
cloned.value.append(4)

print("Original:", original.value)  # Output: Original: [1, 2, 3]
print("Cloned:", cloned.value)       # Output: Cloned: [1, 2, 3, 4]
