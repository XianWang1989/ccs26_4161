
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
                (type(self), new_kwargs) + tuple(new_args),
                state)

class MyObject(Base):
    def __init__(self, value, additional=None):
        self.value = value
        self.additional = additional

    def __deepcopy__(self, memo):
        new, args, state = self.__reduce__()
        result = new(*args)

        if state:
            result.__setstate__(state)

        memo[id(self)] = result

        # Here, we can also handle additional options if necessary
        if hasattr(self, 'additional'):
            result.additional = copy.deepcopy(self.additional, memo)

        return result

# Example usage
obj1 = MyObject(value=42, additional=[1, 2, 3])
obj2 = copy.deepcopy(obj1)

print(obj1.value)        # Output: 42
print(obj2.value)       # Output: 42
print(obj1.additional)   # Output: [1, 2, 3]
print(obj2.additional)   # Output: [1, 2, 3]
