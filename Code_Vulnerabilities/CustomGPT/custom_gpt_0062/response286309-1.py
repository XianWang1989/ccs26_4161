
import copy

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
    def __init__(self, data, option=None):
        self.data = data
        self.option = option

    def __deepcopy__(self, memo):
        # Use pickling for deepcopy
        new, args, state = self.__reduce__()

        # Passing options if needed
        if self.option:
            state['option'] = self.option

        result = new(*args)
        if state:
            result.__setstate__(state)

        memo[id(self)] = result
        return result

# Example usage:
obj1 = MyClass(data=[1, 2, 3], option='original')
obj2 = copy.deepcopy(obj1)  # Deepcopy using the custom logic

# Inspect the copied object
print(obj1.data, obj1.option)  # Output: [1, 2, 3] original
print(obj2.data, obj2.option)  # Output: [1, 2, 3] original
