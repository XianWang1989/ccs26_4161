
import copy

class Base:
    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getstate__(self):
        return {}  # Customize state attributes if needed

    def __setstate__(self, state):
        self.__dict__.update(state)

    def __getnewargs_ex__(self):
        return ((), {})  # Default args and kwargs

    def __reduce__(self):
        new_args, new_kwargs = self.__getnewargs_ex__()
        state = self.__getstate__()
        return (type(self).kwargs_new,
                (type(self), new_kwargs) + tuple(new_args),
                state)

class MyObject(Base):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __deepcopy__(self, memo):
        # Use the custom __reduce__ method for deepcopying
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)

        memo[id(self)] = result
        return result

# Example usage
obj1 = MyObject('example', 42)
deep_copied_obj = copy.deepcopy(obj1)

print(deep_copied_obj.name)  # Output: example
print(deep_copied_obj.value)  # Output: 42

# Modify the original
obj1.name = 'changed'
print(obj1.name)             # Output: changed
print(deep_copied_obj.name)  # Output: example (remains unchanged)
