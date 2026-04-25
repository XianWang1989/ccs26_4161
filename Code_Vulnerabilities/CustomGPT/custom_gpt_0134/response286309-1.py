
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
        return (type(self).kwargs_new, (type(self), new_kwargs) + tuple(new_args), state)


class MyClass(Base):
    def __init__(self, value):
        self.value = value

    def __deepcopy__(self, memo):
        # Use __reduce__ to create a deepcopy based on pickling
        new, args, state = self.__reduce__()
        result = new(*args)

        if state:
            result.__setstate__(state)

        memo[id(self)] = result
        return result


# Example Usage
obj1 = MyClass(5)
obj2 = copy.deepcopy(obj1)

print(obj1.value)  # Output: 5
print(obj2.value)  # Output: 5

obj2.value = 10
print(obj1.value)  # Output: 5 (original remains unchanged)
print(obj2.value)  # Output: 10 (deep copy can be modified)
