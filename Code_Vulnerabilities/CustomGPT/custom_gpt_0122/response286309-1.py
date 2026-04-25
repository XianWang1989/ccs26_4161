
import copy

class MyBase:
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
                (type(self), new_kwargs,) + tuple(new_args),
                state)

class MyClass(MyBase):
    def __init__(self, value):
        self.value = value

    def __deepcopy__(self, memo):
        # Implement deepcopy using __reduce__
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result

# Example usage
if __name__ == "__main__":
    original = MyClass(42)
    copy_instance = copy.deepcopy(original)

    print(f"Original value: {original.value}")
    print(f"Copied value: {copy_instance.value}")
