
import pickle

class CustomClass:
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
        return (type(self).kwargs_new, (type(self), new_kwargs) + tuple(new_args), state)

    def __deepcopy__(self, memo, options=None):
        # Unpickling mechanism for deepcopy
        new, args, state = self.__reduce__()
        result = new(*args)

        # Here you can implement custom option handling
        if options and 'skip' in options:
            for key in options['skip']:
                if key in state:
                    del state[key]

        if state:
            result.__setstate__(state)

        memo[id(self)] = result
        return result

# Example usage:
obj = CustomClass()
obj.attr1 = 'value1'
obj.attr2 = 'value2'
print("Original Object:", obj.__dict__)

# Perform a deepcopy with an option to skip 'attr2'
deep_copied_obj = obj.__deepcopy__({}, options={'skip': ['attr2']})
print("Deep Copied Object:", deep_copied_obj.__dict__)

# Verify original object's attributes remain unchanged
print("After Deep Copy - Original Object:", obj.__dict__)
