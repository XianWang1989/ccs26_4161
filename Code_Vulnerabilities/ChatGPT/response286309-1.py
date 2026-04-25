
import pickle

class MyBaseClass:
    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getstate__(self):
        # Implement this to return the state to pickle
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__.update(state)

    def __getnewargs_ex__(self):
        return ((), {})

    def __reduce__(self):
        new_args, new_kwargs = self.__getnewargs_ex__()
        state = self.__getstate__()
        return (type(self).kwargs_new, (type(self), new_kwargs) + tuple(new_args), state)


class MyClass(MyBaseClass):
    def __init__(self, data):
        self.data = data
        self.more_data = [1, 2, 3]

    def __deepcopy__(self, memo):
        # Prevent endless recursion
        if id(self) in memo:
            return memo[id(self)]

        # Use pickle for deep copying
        copied_obj = pickle.loads(pickle.dumps(self))
        memo[id(self)] = copied_obj
        return copied_obj

    def __repr__(self):
        return f"MyClass(data={self.data}, more_data={self.more_data})"


# Example usage
if __name__ == "__main__":
    original = MyClass(data="Hello World")
    copied = deepcopy(original)

    print("Original:", original)
    print("Copied:", copied)

    # Modifying the copied object's data to show that it's truly a deep copy
    copied.data = "New Data"
    copied.more_data.append(4)

    print("\nAfter modification:")
    print("Original:", original)
    print("Copied:", copied)
