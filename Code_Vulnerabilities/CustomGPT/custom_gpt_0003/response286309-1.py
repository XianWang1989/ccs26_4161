
import copy

class Base:
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
        return (type(self).kwargs_new, (type(self), new_kwargs,) + tuple(new_args), state)


class MyClass(Base):
    def __init__(self, value):
        self.value = value
        self.children = []

    def __deepcopy__(self, memo):
        # Use the base class's __reduce__ for initial setup
        new, args, state = self.__reduce__()
        result = new(*args)  # Create a new instance
        memo[id(self)] = result  # Track the object in memo for recursion
        if state:
            result.__setstate__(state)  # Set state if present

        # Additionally deepcopy child objects
        result.children = copy.deepcopy(self.children, memo)
        return result

# Example usage
if __name__ == "__main__":
    obj1 = MyClass(10)
    obj2 = MyClass(20)

    # Establishing a parent-child relationship
    obj1.children.append(obj2)

    # Creating a deep copy of obj1
    obj_copy = copy.deepcopy(obj1)

    print(f"Original value: {obj1.value}, Child value: {obj1.children[0].value}")
    print(f"Copied value: {obj_copy.value}, Child value: {obj_copy.children[0].value}")

    # Modifying the copy to show that it is indeed a deep copy
    obj_copy.value = 30
    obj_copy.children[0].value = 40

    print(f"After modification - Original value: {obj1.value}, Child value: {obj1.children[0].value}")
    print(f"After modification - Copied value: {obj_copy.value}, Child value: {obj_copy.children[0].value}")
