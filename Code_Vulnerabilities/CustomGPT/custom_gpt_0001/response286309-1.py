
import copy

class CustomObject:
    def __init__(self, name, value, additional_info=None):
        self.name = name
        self.value = value
        self.additional_info = additional_info

    def __deepcopy__(self, memo, **options):
        # Use the pickling approach
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)

        memo[id(self)] = result

        # Handle options for copying
        if options.get('copy_additional_info', True):
            result.additional_info = copy.deepcopy(self.additional_info, memo)

        return result

    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getstate__(self):
        return {
            'name': self.name,
            'value': self.value,
            'additional_info': self.additional_info
        }

    def __setstate__(self, state):
        self.name = state['name']
        self.value = state['value']
        self.additional_info = state.get('additional_info', None)

    def __getnewargs_ex__(self):
        return ((), {})

    def __reduce__(self):
        new_args, new_kwargs = self.__getnewargs_ex__()
        state = self.__getstate__()
        return (type(self).kwargs_new,
                (type(self), new_kwargs,) + tuple(new_args),
                state)


# Example usage
original = CustomObject("example", 42, {"info": "original"})
deep_copied = copy.deepcopy(original, copy_additional_info=True)

# Modify copied object's additional_info to demonstrate it's a true deep copy
deep_copied.additional_info["info"] = "copied"

print(original.additional_info)  # Output: {'info': 'original'}
print(deep_copied.additional_info)  # Output: {'info': 'copied'}
