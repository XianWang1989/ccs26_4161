
import copy

class CustomClass:
    def __init__(self, data, important_attr=None):
        self.data = data
        self.important_attr = important_attr

    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getstate__(self):
        return {'data': self.data, 'important_attr': self.important_attr}

    def __setstate__(self, state):
        self.data = state['data']
        self.important_attr = state['important_attr']

    def __getnewargs_ex__(self):
        return ((), {})

    def __reduce__(self):
        new_args, new_kwargs = self.__getnewargs_ex__()
        state = self.__getstate__()
        return (type(self).kwargs_new, (type(self), new_kwargs,) + tuple(new_args), state)

    def __deepcopy__(self, memo, options=None):
        if options is None:
            options = {}

        # Utilize __reduce__ for picking and unpicking.
        new, args, state = self.__reduce__()
        result = new(*args)

        if state:
            result.__setstate__(state)

        memo[id(self)] = result

        # Handle options (for demonstration purposes)
        if options.get('copy_important_attr', True):
            result.important_attr = copy.deepcopy(self.important_attr, memo)

        return result


# Example usage
original = CustomClass(data=[1, 2, 3], important_attr={'key': 'value'})
print('Original:', original.data, original.important_attr)

# Passing options to deepcopy
options = {'copy_important_attr': True}
copied = copy.deepcopy(original, options=options)

print('Copied:', copied.data, copied.important_attr)
