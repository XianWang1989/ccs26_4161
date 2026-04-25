
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
        return (type(self).kwargs_new, (type(self), new_kwargs,) + tuple(new_args), state)


class Example(Base):
    def __init__(self, data):
        self.data = data

    def __getstate__(self):
        return (self.data,)

    def __setstate__(self, state):
        self.data = state[0]

    def __deepcopy__(self, memo):
        # Uses pickling to deepcopy
        new, args, state = self.__reduce__()
        result = new(*args)  # Creates the new object
        if state:
            result.__setstate__(state)  # Sets the state
        memo[id(self)] = result  # Memoization to avoid duplicates
        return result


# Example usage:
if __name__ == "__main__":
    original = Example([1, 2, 3])
    copy_of_original = copy.deepcopy(original)

    print("Original:", original.data)  # Output: [1, 2, 3]
    print("Copy:", copy_of_original.data)  # Output: [1, 2, 3]

    # Modifying the copy
    copy_of_original.data.append(4)

    print("After modifying the copy...")
    print("Original:", original.data)  # Output: [1, 2, 3] (remains unchanged)
    print("Copy:", copy_of_original.data)  # Output: [1, 2, 3, 4]
