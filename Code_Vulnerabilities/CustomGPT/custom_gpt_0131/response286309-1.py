
import copy

class CustomObject:
    def __init__(self, value, options=None):
        self.value = value
        self.options = options if options is not None else {}

    def __getstate__(self):
        return self.value, self.options

    def __setstate__(self, state):
        self.value, self.options = state

    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getnewargs_ex__(self):
        return ((), {'options': self.options})

    def __reduce__(self):
        new_args, new_kwargs = self.__getnewargs_ex__()
        state = self.__getstate__()
        return (type(self).kwargs_new,
                (type(self), new_kwargs) + tuple(new_args),
                state)

    def __deepcopy__(self, memo):
        # Use __reduce__ for pickling
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)

        # Here you might add additional options handling logic
        if self.options.get('copy_value', True):
            result.value = copy.deepcopy(self.value, memo)

        memo[id(self)] = result
        return result

# Example of usage
original = CustomObject(value=[1, 2, 3], options={'copy_value': True})
deep_copied = copy.deepcopy(original)

print('Original:', original.value)  # Output: Original: [1, 2, 3]
print('Deep Copied:', deep_copied.value)  # Output: Deep Copied: [1, 2, 3]

# Modifying the deep copy
deep_copied.value.append(4)

print('After modification:')
print('Original:', original.value)  # Output: Original: [1, 2, 3]
print('Deep Copied:', deep_copied.value)  # Output: Deep Copied: [1, 2, 3, 4]
