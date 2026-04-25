
import copy
import copyreg

class MyClass:
    def __init__(self, data):
        self.data = data

    def __getstate__(self):
        return (self.data,)

    def __setstate__(self, state):
        self.data, = state

    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __reduce__(self):
        return (self.kwargs_new, (self.__class__, {}, self.data), self.__getstate__())

    def __deepcopy__(self, memo):
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result

# Example usage
obj1 = MyClass([1, 2, 3])
obj2 = copy.deepcopy(obj1)

print(obj1.data)  # Output: [1, 2, 3]
print(obj2.data)  # Output: [1, 2, 3]

obj2.data.append(4)
print(obj1.data)  # Output: [1, 2, 3]
print(obj2.data)  # Output: [1, 2, 3, 4]
