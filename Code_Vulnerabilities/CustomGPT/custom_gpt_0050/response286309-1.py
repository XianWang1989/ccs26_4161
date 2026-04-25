
import copy

class CustomClass:
    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__.update(state)

    def __getnewargs_ex__(self):
        return ((), {})

    def __reduce__(self):
        new_args, new_kwargs = self.__getnewargs_ex__()
        state = self.__getstate__()
        return (type(self).kwargs_new, (type(self), new_kwargs) + tuple(new_args), state)

    def __deepcopy__(self, memo):
        # Use the __reduce__ method to get the new instance
        new, args, state = self.__reduce__()
        result = new(*args)

        if state:
            result.__setstate__(state)

        # Store the result in memo to handle cyclic references
        memo[id(self)] = result
        return result

# Example of usage
if __name__ == "__main__":
    original = CustomClass()
    original.some_attr = [1, 2, 3]

    # Create a deep copy
    copied = copy.deepcopy(original)

    print("Original:", original.some_attr)
    print("Copied:", copied.some_attr)

    # Modify the copied object's attribute
    copied.some_attr.append(4)

    print("After modification:")
    print("Original:", original.some_attr)  # Should remain unchanged
    print("Copied:", copied.some_attr)      # Should show [1, 2, 3, 4]
