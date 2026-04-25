
import copy

class CustomObject:
    def __init__(self, value):
        self.value = value
        self._private = "I'm private"

    def __getstate__(self):
        # Control what is pickled
        return {
            'value': self.value,
            # Exclude private attributes or manage them as needed
        }

    def __setstate__(self, state):
        # Recover state from the dictionary
        self.value = state['value']
        self._private = "Restored private attribute"

    def __deepcopy__(self, memo):
        # Utilize pickling for deep copy
        if id(self) in memo:
            return memo[id(self)]

        # Call __reduce__ to get new instance and state
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)

        memo[id(self)] = result
        return result

    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __reduce__(self):
        new_args = (self.value,)
        state = self.__getstate__()
        return (type(self).kwargs_new, (type(self), {},) + new_args, state)

# Example usage
obj1 = CustomObject("Hello")
deep_copied_obj = copy.deepcopy(obj1)

print(deep_copied_obj.value)        # Output: Hello
print(deep_copied_obj._private)     # Output: Restored private attribute
