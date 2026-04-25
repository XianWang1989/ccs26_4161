
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
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __deepcopy__(self, memo):
        # Check if the object has already been copied
        if id(self) in memo:
            return memo[id(self)]

        # Use pickling to deepcopy
        new, args, state = self.__reduce__()
        result = new(*args)

        if state:
            result.__setstate__(state)

        memo[id(self)] = result

        return result

# Example Usage
original = MyClass("test", 42)
copy_instance = copy.deepcopy(original)

print(original.name, original.value)  # Output: test 42
print(copy_instance.name, copy_instance.value)  # Output: test 42
