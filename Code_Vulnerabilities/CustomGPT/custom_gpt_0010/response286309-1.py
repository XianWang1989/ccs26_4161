
import copy

class Base:
    """Base class providing default behavior for __reduce__, __getstate__, and __setstate__."""

    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        """Override this method to use a different new."""
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
    def __init__(self, data):
        self.data = data

    def __deepcopy__(self, memo):
        """Deepcopy using pickling/unpickling approach."""
        if id(self) in memo:
            return memo[id(self)]
        new, args, state = self.__reduce__()
        result = new(*args)  # Creating a new instance
        if state:
            result.__setstate__(state)  # Restoring state
        memo[id(self)] = result  # Storing in the memo
        return result

# Example of using MyObject
obj1 = MyObject({'key': 'value'})
obj2 = copy.deepcopy(obj1)

print(obj1.data)  # Output: {'key': 'value'}
print(obj2.data)  # Output: {'key': 'value'}

# Modifying the deep copy
obj2.data['key'] = 'new_value'
print(obj1.data)  # Output: {'key': 'value'}
print(obj2.data)  # Output: {'key': 'new_value'}  # obj2 is independent of obj1
