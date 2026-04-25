
import pickle

class MyBaseClass:
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


class MyClass(MyBaseClass):
    def __init__(self, value):
        self.value = value

    def __deepcopy__(self, memo):
        # Use pickle for deepcopy
        if id(self) in memo:
            return memo[id(self)]

        result = pickle.loads(pickle.dumps(self))
        memo[id(self)] = result
        return result

# Example usage
if __name__ == "__main__":
    obj1 = MyClass(10)
    obj2 = obj1.__deepcopy__({})

    print(obj1.value)  # Output: 10
    print(obj2.value)  # Output: 10

    obj2.value = 20
    print(obj1.value)  # Output: 10 (original object remains unchanged)
    print(obj2.value)  # Output: 20 (deep copied object modified)
