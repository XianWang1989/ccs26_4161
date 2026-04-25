import copy
import pickle

class CustomCopyBase:
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
        return (), {}

    def __reduce__(self):
        new_args, new_kwargs = self.__getnewargs_ex__()
        state = self.__getstate__()
        return (
            type(self).kwargs_new,
            (type(self), new_kwargs) + tuple(new_args),
            state
        )

    def __deepcopy__(self, memo):
        options = memo.get('options', {})  # Get custom options from memo if provided
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            # Optionally customize state before setting
            if 'exclude' in options:
                for key in options['exclude']:
                    state.pop(key, None)
            result.__setstate__(state)
        memo[id(self)] = result
        return result

# Example usage
class MyClass(CustomCopyBase):
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = MyClass(10, 20)

# Custom deepcopy with exclusion option
memo = {'options': {'exclude': ['y']}}
copied = copy.deepcopy(obj, memo)

print(copied.__dict__)  # Output: {'x': 10}
