
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
        return (type(self).kwargs_new,
                (type(self), new_kwargs,) + tuple(new_args),
                state)

class MyClass(Base):
    def __init__(self, data):
        self.data = data

    def __deepcopy__(self, memo):
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result

    def __repr__(self):
        return f"MyClass({self.data!r})"

# Example usage
if __name__ == "__main__":
    original = MyClass({'key': 'value'})
    copied = copy.deepcopy(original)

    print(f"Original: {original}")
    print(f"Copied: {copied}")

    # Change the original to show that the deepcopy worked
    original.data['key'] = 'new_value'
    print(f"After modification:\nOriginal: {original}\nCopied: {copied}")
