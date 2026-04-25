
import copy

class BaseClass:
    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getstate__(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}

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

class MyClass(BaseClass):
    def __init__(self, attr1, attr2, attr3):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3

    def __deepcopy__(self, memo, options=None):
        # Default deepcopy behavior
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)

        memo[id(self)] = result

        # If options are provided, utilize them for selective copying
        if options and "copy_attrs" in options:
            for attr in options["copy_attrs"]:
                if hasattr(self, attr):
                    setattr(result, attr, copy.deepcopy(getattr(self, attr), memo))
        else:
            for k, v in self.__dict__.items():
                setattr(result, k, copy.deepcopy(v, memo))

        return result

# Example usage
original = MyClass("value1", "value2", "value3")
options = {"copy_attrs": ["attr1", "attr2"]}
copied = copy.deepcopy(original, options=options)

print("Original:", original.__dict__)
print("Copied:", copied.__dict__)
