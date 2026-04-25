
import copy

class BaseClass:
    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        """
        Override this method to use a different new.
        """
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

class MyObject(BaseClass):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __deepcopy__(self, memo):
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result

# Example usage
if __name__ == "__main__":
    obj1 = MyObject("Example", 42)
    obj2 = copy.deepcopy(obj1)

    print(f"Original: {obj1.name}, {obj1.value}")
    print(f"Copied: {obj2.name}, {obj2.value}")
