
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
        return (type(self).kwargs_new, (type(self), new_kwargs) + tuple(new_args), state)


class MyClass(Base):
    def __init__(self, data):
        self.data = data

    def __deepcopy__(self, memo):
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result

        # Here you can customize the deepcopy for specific attributes if needed
        # For example, let's assume you want to deepcopy only specific attributes
        # if required:

        # Uncomment and modify the following lines as needed for custom behavior
        # for k, v in self.__dict__.items():
        #     if k in ['data']:  # Specify attributes you want to deepcopy
        #         setattr(result, k, copy.deepcopy(v, memo))

        return result

# Example usage
original = MyClass([1, 2, 3])
deep_copied = copy.deepcopy(original)

print("Original data:", original.data)
print("Deep copied data:", deep_copied.data)
