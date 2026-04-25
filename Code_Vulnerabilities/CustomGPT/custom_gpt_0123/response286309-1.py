
import copy
import pickle

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
                (type(self), new_kwargs) + tuple(new_args),
                state)

class MyClass(Base):
    def __init__(self, data):
        self.data = data

    def __deepcopy__(self, memo, options=None):
        # Use a custom approach if options exist
        if options:
            # Example: ignore certain attributes during copy
            if 'ignore' in options and options['ignore']:
                temp_data = {k: v for k, v in self.__dict__.items() if k not in options['ignore']}
                new_instance = MyClass(None)
                new_instance.__dict__.update(temp_data)
                memo[id(self)] = new_instance
                return new_instance

        # Default deepcopy using pickling
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result

# Example usage:
obj1 = MyClass(data="important data")
memo = {}
options = {'ignore': ['data']}  # Ignoring 'data' during deepcopy
obj2 = copy.deepcopy(obj1, memo, options)

print(obj1.__dict__)  # {'data': 'important data'}
print(obj2.__dict__)  # {}
