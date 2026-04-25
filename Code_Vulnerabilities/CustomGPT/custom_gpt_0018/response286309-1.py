
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
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __deepcopy__(self, memo):
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result

# Example usage:
original = MyClass(1, [2, 3, 4])
deep_copied = copy.deepcopy(original)

print(f"Original: a={original.a}, b={original.b}")
print(f"Deep Copied: a={deep_copied.a}, b={deep_copied.b}")

# Modify the original to show that the deep copy is independent
original.b.append(5)

print(f"After modification, Original: a={original.a}, b={original.b}")
print(f"After modification, Deep Copied: a={deep_copied.a}, b={deep_copied.b}")
