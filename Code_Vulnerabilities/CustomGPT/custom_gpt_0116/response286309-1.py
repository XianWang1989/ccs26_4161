
import pickle

class MyClass:
    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getstate__(self):
        # Customize what gets pickled
        return self.__dict__.copy()

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

    def __deepcopy__(self, memo):
        # Custom deepcopy using pickle
        if id(self) in memo:
            return memo[id(self)]

        # Pickle and unpickle
        result = pickle.loads(pickle.dumps(self))
        memo[id(self)] = result
        return result

# Example usage
obj1 = MyClass()
obj1.data = [1, 2, 3]

# Perform a deepcopy
obj2 = obj1.__deepcopy__({})
print(obj2.data)  # Output: [1, 2, 3]

# Changing the original object does not affect the deepcopy
obj1.data.append(4)
print(obj1.data)  # Output: [1, 2, 3, 4]
print(obj2.data)  # Output: [1, 2, 3]
