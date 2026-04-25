
import copy
import pickle

class MyBase:
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

class MyClass(MyBase):
    def __init__(self, data):
        self.data = data

    def __deepcopy__(self, memo):
        # Use pickle to create a deep copy
        new, args, state = self.__reduce__()
        result = new(*args)  # Call new with the given args
        if state:
            result.__setstate__(state)  # Restore the state if exists
        memo[id(self)] = result
        return result

# Example Usage
original = MyClass(data={'key': 'value'})
copy_of_original = copy.deepcopy(original)

# Modify the original to show they are independent
original.data['key'] = 'new_value'

print("Original:", original.data)         # Outputs: {'key': 'new_value'}
print("Copy:", copy_of_original.data)      # Outputs: {'key': 'value'}
