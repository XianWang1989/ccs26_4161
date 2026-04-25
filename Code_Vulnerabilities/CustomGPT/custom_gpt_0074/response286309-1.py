
import copy

class ExampleClass:
    def __init__(self, value):
        self.value = value
        self.options = {}

    def __deepcopy__(self, memo, options=None):
        memo[id(self)] = result = self.__reduce__()[0](*self.__reduce__()[1])
        if options and 'update_value' in options:
            result.value = options['update_value']
        return result

    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__.update(state)

    def __reduce__(self):
        return (self.kwargs_new, (self.__class__, {}, self.value), self.__getstate__)
