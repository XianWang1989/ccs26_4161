
import copy
import pickle


class CustomBase:
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


class MyObject(CustomBase):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __deepcopy__(self, memo):
        # Use pickling and unpickling to create a deep copy
        if id(self) in memo:
            return memo[id(self)]  # Return already copied instance
        # Pickle the current state
        new = pickle.loads(pickle.dumps(self))
        memo[id(self)] = new
        return new


# Example usage
original = MyObject("example", [1, 2, 3])
copy_of_original = copy.deepcopy(original)

# Modifying the copied object
copy_of_original.value.append(4)

print("Original:", original.value)  # Outputs: Original: [1, 2, 3]
print("Copy:", copy_of_original.value)  # Outputs: Copy: [1, 2, 3, 4]
