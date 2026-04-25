
import copy

class CustomClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getstate__(self):
        return {'name': self.name, 'value': self.value}

    def __setstate__(self, state):
        self.name = state['name']
        self.value = state['value']

    def __getnewargs_ex__(self):
        return ((), {})

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

# Example Usage
if __name__ == "__main__":
    obj1 = CustomClass("Test", 42)
    obj2 = copy.deepcopy(obj1)

    print(f"Original: {obj1.name}, {obj1.value}")  # Output: Original: Test, 42
    print(f"Deepcopied: {obj2.name}, {obj2.value}")  # Output: Deepcopied: Test, 42

    # Modify the original object
    obj1.name = "Changed"
    print(f"After change - Original: {obj1.name}, Deepcopied: {obj2.name}")  # Output: Original: Changed, Deepcopied: Test
