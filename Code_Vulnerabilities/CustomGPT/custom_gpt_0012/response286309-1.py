
import pickle

class MyClass:
    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getstate__(self):
        # Return the state for pickling
        return self.__dict__

    def __setstate__(self, state):
        # Restore state for unpickling
        self.__dict__.update(state)

    def __getnewargs_ex__(self):
        return ((), {})

    def __reduce__(self):
        new_args, new_kwargs = self.__getnewargs_ex__()
        state = self.__getstate__()
        return (type(self).kwargs_new,
                (type(self), new_kwargs,) + tuple(new_args),
                state)

    def __deepcopy__(self, memo):
        # Use pickling to create a deep copy
        return pickle.loads(pickle.dumps(self, protocol=pickle.HIGHEST_PROTOCOL))

# Example usage
obj1 = MyClass()
obj1.value = [1, 2, 3]
obj2 = obj1.__deepcopy__({})  # Create a deep copy of obj1

print(obj1.value)  # Output: [1, 2, 3]
print(obj2.value)  # Output: [1, 2, 3]

obj2.value.append(4)  # Modify the copied object
print(obj1.value)  # Output: [1, 2, 3]
print(obj2.value)  # Output: [1, 2, 3, 4]
