
import copy
import pickle

class MyBaseClass:
    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        """
        Override this method to use a different new.
        """
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
                (type(self), new_kwargs,) + tuple(new_args),
                state)

class MyCustomClass(MyBaseClass):
    def __init__(self, value):
        self.value = value

    def __deepcopy__(self, memo):
        # Use pickle to create a deep copy
        if id(self) in memo:
            return memo[id(self)]

        # Call pickle to create a deep copy
        result = pickle.loads(pickle.dumps(self, protocol=pickle.HIGHEST_PROTOCOL))

        # Add to memo for future reference
        memo[id(self)] = result
        return result

# Example usage
obj = MyCustomClass([1, 2, 3])
deep_copied_obj = copy.deepcopy(obj)

# Modify the original object
obj.value.append(4)

print("Original value:", obj.value)           # Output: [1, 2, 3, 4]
print("Deep copied value:", deep_copied_obj.value)  # Output: [1, 2, 3]
