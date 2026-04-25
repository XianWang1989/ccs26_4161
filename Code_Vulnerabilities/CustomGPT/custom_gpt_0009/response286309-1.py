
import copy
import copyreg

class MyClass:
    # Define your properties and initialization here
    def __init__(self, data):
        self.data = data

    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getstate__(self):
        return self.data  

    def __setstate__(self, state):
        self.data = state  

    def __getnewargs_ex__(self):
        return ((), {})  # Adjust for your args if necessary

    def __reduce__(self):
        new_args, new_kwargs = self.__getnewargs_ex__()
        state = self.__getstate__()
        return (type(self).kwargs_new,
                (type(self), new_kwargs) + tuple(new_args), 
                state)

    def __deepcopy__(self, memo):
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result

# Example usage
original = MyClass(data={'key': 'value'})
copy_of_original = copy.deepcopy(original)

print(f"Original data: {original.data}")
print(f"Copied data: {copy_of_original.data}")
