
import copy

class BaseClass:
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

class MyClass(BaseClass):
    def __init__(self, x):
        self.x = x

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

print(f'Original x: {original.x}')       # Output: Original x: 10
print(f'Deep copied x: {deep_copied.x}') # Output: Deep copied x: 10

# Modifying original
original.x = 20
print(f'After modification - Original x: {original.x}')       # Output: After modification - Original x: 20
print(f'After modification - Deep copied x: {deep_copied.x}') # Output: After modification - Deep copied x: 10
