
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
    def __init__(self, value):
        self.value = value

    def __deepcopy__(self, memo, options=None):
        if options and options.get('use_pickling', True):
            new, args, state = self.__reduce__()
            result = new(*args)
            if state:
                result.__setstate__(state)
        else:
            # Fallback to dict copying if options dictate
            cls = self.__class__
            result = cls.__new__(cls)
            memo[id(self)] = result
            for k, v in self.__dict__.items():
                setattr(result, k, copy.deepcopy(v, memo))

        memo[id(self)] = result
        return result

# Example usage
original = MyClass(10)
deep_copied = copy.deepcopy(original, options={'use_pickling': True})

print(original.value)        # Outputs: 10
print(deep_copied.value)    # Outputs: 10

# Modify original
original.value = 20
print(original.value)        # Outputs: 20
print(deep_copied.value)    # Outputs: 10 (remains unchanged)
