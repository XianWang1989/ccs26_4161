
import pickle
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

    def __deepcopy__(self, memo):
        # Using the __reduce__ mechanism for deepcopy
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result

# Example usage
obj1 = MyClass([1, 2, 3])
obj2 = copy.deepcopy(obj1)

# Modifying obj1 to show that it doesn't affect obj2
obj1.value.append(4)

print("Original object value:", obj1.value)  # Output: [1, 2, 3, 4]
print("Deep copied object value:", obj2.value)  # Output: [1, 2, 3]
