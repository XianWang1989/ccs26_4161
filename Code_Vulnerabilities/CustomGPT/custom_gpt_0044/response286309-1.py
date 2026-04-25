
from copy import deepcopy

class Base:
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

class CustomObject(Base):
    def __init__(self, value, additional=None):
        self.value = value
        self.additional = additional or []

    def __deepcopy__(self, memo, options=None):
        new, args, state = self.__reduce__()
        result = new(*args)

        if options and options.get('skip_additional'):
            result.value = self.value  # Copy only value
        else:
            result.additional = deepcopy(self.additional, memo)  # Deep copy additional if not skipped

        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result

# Example usage
if __name__ == '__main__':
    obj1 = CustomObject(10, [1, 2, 3])
    options = {'skip_additional': True}
    obj2 = deepcopy(obj1, memo={}, options=options)

    print(obj2.value)         # Output: 10
    print(obj2.additional)    # Output: [] (skipped)
