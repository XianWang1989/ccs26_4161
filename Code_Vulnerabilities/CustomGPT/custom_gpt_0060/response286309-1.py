
import pickle

class MyBaseClass:
    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getstate__(self):
        # Customize the state you want to pickle
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
        # Using the default Python pickling mechanism
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result

# Example of a custom class
class MyClass(MyBaseClass):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"MyClass(name={self.name}, age={self.age})"

# Example usage
if __name__ == "__main__":
    original = MyClass("Alice", 30)
    copy = pickle.loads(pickle.dumps(original))  # Create a deepcopy via pickling

    # Now to see the results
    print("Original:", original)
    print("Copy:", copy)

    # Modifying the copy to see if it indeed is a deepcopy
    copy.name = "Bob"
    print("After modification:")
    print("Original:", original)
    print("Copy:", copy)
