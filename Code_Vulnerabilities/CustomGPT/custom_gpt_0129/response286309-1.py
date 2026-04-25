
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
                (type(self), new_kwargs) + tuple(new_args),
                state)


class CustomClass(BaseClass):
    def __init__(self, data):
        self.data = data

    def __deepcopy__(self, memo):
        # Use the reduce function to create a new instance
        new, args, state = self.__reduce__()
        result = new(*args)

        # If state exists, set it
        if state:
            result.__setstate__(state)

        # Keep track of the memoization for deep copies
        memo[id(self)] = result
        return result

    # Sample method to demonstrate behavior
    def display(self):
        return f"Data: {self.data}"


# Example usage
if __name__ == "__main__":
    original = CustomClass(data=[1, 2, 3])
    copied_instance = copy.deepcopy(original)

    original.data[0] = 99  # Modifying the original instance to show deep copy effect

    print(f"Original: {original.display()}")  # Should show modified data
    print(f"Copied: {copied_instance.display()}")  # Should show original data
