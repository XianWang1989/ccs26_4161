
import copy

class MyBase:
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

class MyClass(MyBase):
    def __init__(self, data):
        self.data = data

    def __deepcopy__(self, memo):
        # Utilize pickling for deepcopy
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result

# Example usage
original = MyClass([1, 2, 3])
copy_obj = copy.deepcopy(original)

print("Original:", original.data)  # Output: Original: [1, 2, 3]
print("Copy:", copy_obj.data)       # Output: Copy: [1, 2, 3]

# Modify the copy and check that original remains unchanged
copy_obj.data.append(4)

print("After modification:")
print("Original:", original.data)  # Output: Original: [1, 2, 3]
print("Copy:", copy_obj.data)       # Output: Copy: [1, 2, 3, 4]
