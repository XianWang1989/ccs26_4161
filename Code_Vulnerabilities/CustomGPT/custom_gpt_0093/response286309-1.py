
import copy

class Base:
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
        return (type(self).kwargs_new, (type(self), new_kwargs,) + tuple(new_args), state)


class MyObject(Base):
    def __init__(self, val):
        self.val = val

    def __deepcopy__(self, memo, option=None):
        """Customize deep copy with an additional option."""
        new, args, state = self.__reduce__()
        result = new(*args)

        # Example handling of the option
        if option == 'skip_val':
            state = {k: v for k, v in state.items() if k != 'val'}

        if state:
            result.__setstate__(state)

        memo[id(self)] = result
        return result

# Usage example
if __name__ == "__main__":
    obj1 = MyObject(10)
    obj2 = copy.deepcopy(obj1, memo={}, option='skip_val')

    print(obj1.__dict__)  # {'val': 10}
    print(obj2.__dict__)  # Should not include 'val' if option='skip_val'
