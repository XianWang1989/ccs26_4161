
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

    def __deepcopy__(self, memo, options=None):
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)

        if options and options.get('copy_value'):
            result.value = copy.deepcopy(self.value, memo)

        memo[id(self)] = result
        return result

# Usage example
original = MyClass(value=[1, 2, 3])
copied = copy.deepcopy(original, options={'copy_value': True})

print('Original:', original.value)  # Output: [1, 2, 3]
print('Copied:', copied.value)       # Output: [1, 2, 3]

# Modify the original
original.value.append(4)
print('Modified Original:', original.value)  # Output: [1, 2, 3, 4]
print('Copied after modification:', copied.value)  # Output: [1, 2, 3]
