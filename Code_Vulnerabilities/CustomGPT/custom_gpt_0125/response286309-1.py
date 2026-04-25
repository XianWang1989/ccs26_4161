
import copy

class MyClass:
    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getstate__(self):
        return {'data': self.data}

    def __setstate__(self, state):
        self.data = state['data']

    def __getnewargs_ex__(self):
        return ((), {})

    def __reduce__(self):
        new_args, new_kwargs = self.__getnewargs_ex__()
        state = self.__getstate__()
        return (type(self).kwargs_new, 
                (type(self), new_kwargs) + tuple(new_args), 
                state)

    def __deepcopy__(self, memo):
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result

    def __init__(self, data):
        self.data = data

# Example usage
original = MyClass([1, 2, 3])
deep_copied = copy.deepcopy(original)

print(original.data)  # Output: [1, 2, 3]
print(deep_copied.data)  # Output: [1, 2, 3]
