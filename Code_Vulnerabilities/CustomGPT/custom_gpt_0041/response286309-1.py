
import copy

class MyClass:
    # Static method for creating an instance with keyword arguments
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
        return ((), {})  # Returning empty args for demonstration

    def __reduce__(self):
        new_args, new_kwargs = self.__getnewargs_ex__()
        state = self.__getstate__()
        return (type(self).kwargs_new, (type(self), new_kwargs) + tuple(new_args), state)

    def __deepcopy__(self, memo):
        # Utilize the __reduce__ method
        new, args, state = self.__reduce__()
        result = new(*args)  # Create a new instance
        if state:
            result.__setstate__(state)  # Restore the state
        memo[id(self)] = result
        return result

# Example usage
if __name__ == "__main__":
    obj1 = MyClass()
    obj1.attr1 = [1, 2, 3]
    obj1.attr2 = 'Hello'

    # Deep copy the object
    obj2 = copy.deepcopy(obj1)

    # Modify the copy to show it's independent
    obj2.attr1.append(4)

    print(obj1.attr1)  # Output: [1, 2, 3]
    print(obj2.attr1)  # Output: [1, 2, 3, 4]
