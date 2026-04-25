
import copy
import pickle

class MyBaseClass:
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
        return (type(self).kwargs_new,
                (type(self), new_kwargs) + tuple(new_args),
                state)

class MyClass(MyBaseClass):
    def __init__(self, my_attr):
        self.my_attr = my_attr

    def __deepcopy__(self, memo):
        # Use pickle to create a deep copy
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result

# Example usage
original = MyClass([1, 2, 3])
deep_copied = copy.deepcopy(original)

print("Original:", original.my_attr)
print("Deep Copied:", deep_copied.my_attr)

# Modify the deep copy
deep_copied.my_attr.append(4)

print("After modification:")
print("Original:", original.my_attr)  # Should be [1, 2, 3]
print("Deep Copied:", deep_copied.my_attr)  # Should be [1, 2, 3, 4]
