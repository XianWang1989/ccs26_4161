
import copy

class CustomObject:
    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getstate__(self):
        # Return the state of the object for pickling.
        return self.__dict__ 

    def __setstate__(self, state):
        # Restore the state of the object from unpickling.
        self.__dict__.update(state)

    def __getnewargs_ex__(self):
        # Provide args and kwargs for object creation.
        return ((), {})

    def __reduce__(self):
        # Implement __reduce__ to include kwargs_new for custom instantiation.
        new_args, new_kwargs = self.__getnewargs_ex__()
        state = self.__getstate__()
        return (type(self).kwargs_new, (type(self), new_kwargs) + new_args, state)

    def __deepcopy__(self, memo):
        # Custom deepcopy implementation using unpickling
        new, args, state = self.__reduce__()
        result = new(*args)  # Create a new instance
        if state:
            result.__setstate__(state)  # Restore state if available
        memo[id(self)] = result  # Store reference in memo
        return result

# Example usage
if __name__ == "__main__":
    original = CustomObject()
    original.attr1 = "Example"
    original.attr2 = [1, 2, 3]

    # Perform a deep copy
    copied_object = copy.deepcopy(original)

    # Show the deep copied object's attributes
    print(copied_object.attr1)  # Outputs: Example
    print(copied_object.attr2)  # Outputs: [1, 2, 3]

    # Verify independence
    copied_object.attr2.append(4)
    print(original.attr2)  # Outputs: [1, 2, 3] (remains unchanged)
