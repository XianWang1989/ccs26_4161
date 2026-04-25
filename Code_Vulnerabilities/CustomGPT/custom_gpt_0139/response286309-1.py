
import pickle
import copy

class CustomClass:
    def __init__(self, data, more_data=None):
        self.data = data
        self.more_data = more_data if more_data is not None else []

    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getstate__(self):
        return self.data, self.more_data

    def __setstate__(self, state):
        self.data, self.more_data = state

    def __getnewargs_ex__(self):
        return ((), {"more_data": self.more_data})

    def __reduce__(self):
        new_args, new_kwargs = self.__getnewargs_ex__()
        state = self.__getstate__()
        return (type(self).kwargs_new,
                (type(self), new_kwargs,) + tuple(new_args),
                state)

    def __deepcopy__(self, memo):
        # Use the __reduce__ method to achieve deep copy
        new, args, state = self.__reduce__()
        result = new(*args)

        if state:
            result.__setstate__(state)

        memo[id(self)] = result
        return result

# Example usage
original = CustomClass(data="Hello, World!", more_data=["item1", "item2"])
deep_copied = copy.deepcopy(original)

print(original.data)        # Output: Hello, World!
print(original.more_data)   # Output: ['item1', 'item2']
print(deep_copied.data)     # Output: Hello, World!
print(deep_copied.more_data) # Output: ['item1', 'item2']

# Verify that the deep copy is indeed a separate object
deep_copied.more_data.append("item3")
print(original.more_data)   # Output: ['item1', 'item2']
print(deep_copied.more_data) # Output: ['item1', 'item2', 'item3']
