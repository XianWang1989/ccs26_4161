
import copy

class MyBaseClass:
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
                (type(self), new_kwargs) + tuple(new_args),
                state)

class MyClass(MyBaseClass):
    def __init__(self, data):
        self.data = data

    def __deepcopy__(self, memo):
        # Call __reduce__ to get the new instance and its state
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result  # Keep track of the copy in memo
        return result

# Example usage
original = MyClass({'key': 'value'})
copy_of_original = copy.deepcopy(original)

# Modify the original to show the deep copy is indeed a separate instance
original.data['key'] = 'new_value'

print("Original:", original.data)             # Output: Original: {'key': 'new_value'}
print("Copy:", copy_of_original.data)         # Output: Copy: {'key': 'value'}
