
import copy

class MyBaseClass:
    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getstate__(self):
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

class MyClass(MyBaseClass):
    def __init__(self, value):
        self.value = value

    def __deepcopy__(self, memo, custom_option=None):
        new, args, state = self.__reduce__()
        result = new(*args)

        # Modify behavior based on custom_option if needed
        if custom_option == 'omit_value':
            # Prevent copying this specific attribute
            result.__dict__.pop('value', None)

        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result

# Example usage
obj1 = MyClass(10)
memo = {}
obj2 = copy.deepcopy(obj1, memo, custom_option='omit_value')

print(obj2.__dict__)  # Should not include 'value' if omitted
