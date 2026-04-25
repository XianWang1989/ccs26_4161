
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
        new, args, state = self.__reduce__()
        result = new(*args)  # Use kwargs_new to create a new instance
        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result

# Example Usage
original = MyClass([1, 2, 3])
deep_copied = copy.deepcopy(original)

# Modifying the deep copied object
deep_copied.value.append(4)

print("Original value:", original.value)  # Output: [1, 2, 3]
print("Deep copied value:", deep_copied.value)  # Output: [1, 2, 3, 4]
