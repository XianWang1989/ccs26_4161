
import copy

class CustomObject:
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

    def __deepcopy__(self, memo, options=None):
        if options and 'skip_attributes' in options:
            state = self.__getstate__()
            # Skip certain attributes if specified in options
            for attr in options['skip_attributes']:
                state.pop(attr, None)
            result = self.__class__.__new__(self.__class__)
            memo[id(self)] = result
            result.__setstate__(state)
            return result

        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result

# Example usage
obj1 = CustomObject()
obj1.attr1 = "value1"
obj1.attr2 = "value2"

# Deepcopy without options
obj2 = copy.deepcopy(obj1)

# Deepcopy with options to skip 'attr2'
obj3 = copy.deepcopy(obj1, options={'skip_attributes': ['attr2']})

print(obj1.__dict__)  # {'attr1': 'value1', 'attr2': 'value2'}
print(obj2.__dict__)  # {'attr1': 'value1', 'attr2': 'value2'}
print(obj3.__dict__)  # {'attr1': 'value1'}
