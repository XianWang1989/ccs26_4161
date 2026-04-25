
import copy

class Base:
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
        return (type(self).kwargs_new, (type(self), new_kwargs) + new_args, state)

class MyClass(Base):
    def __init__(self, data):
        self.data = data

    def __deepcopy__(self, memo):
        # Use pickling to create a deepcopy
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result

# Example usage
original = MyClass(data={'key': 'value'})
deep_copied = copy.deepcopy(original)

# Modifying the deep copied object
deep_copied.data['key'] = 'modified value'

print(original.data)  # Output: {'key': 'value'}
print(deep_copied.data)  # Output: {'key': 'modified value'}
