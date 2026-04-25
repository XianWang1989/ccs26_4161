
import copy
import pickle

class Base:
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
                (type(self), new_kwargs,) + tuple(new_args),
                state)

class CustomObject(Base):
    def __init__(self, data):
        self.data = data

    def __deepcopy__(self, memo):
        # Use pickling and unpickling for deepcopy
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result

# Example usage
if __name__ == "__main__":
    obj1 = CustomObject({'key': 'value'})
    obj2 = copy.deepcopy(obj1)

    print("Original object:", obj1.data)
    print("Deepcopied object:", obj2.data)
