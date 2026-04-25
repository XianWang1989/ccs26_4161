
import copy

class BaseClass:
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

class MyClass(BaseClass):
    def __init__(self, data):
        self.data = data

    def __deepcopy__(self, memo):
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result

# Example of usage
original_object = MyClass(data={'key': 'value'})
copied_object = copy.deepcopy(original_object)

print(original_object.data)  # Output: {'key': 'value'}
print(copied_object.data)    # Output: {'key': 'value'}

# Modify the copied object's data
copied_object.data['key'] = 'new_value'
print(original_object.data)  # Output: {'key': 'value'}
print(copied_object.data)    # Output: {'key': 'new_value'}
