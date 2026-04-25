
import copy

class MyBase:
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
                (type(self), new_kwargs,) + tuple(new_args),
                state)

class MyObject(MyBase):
    def __init__(self, data):
        self.data = data
        self.other = [1, 2, 3]

    def __deepcopy__(self, memo):
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)
        memo[id(self)] = result
        return result

# Example usage
obj1 = MyObject("Hello")
obj2 = copy.deepcopy(obj1)

print(obj1.data)  # Output: Hello
print(obj2.data)  # Output: Hello
print(obj1.other)  # Output: [1, 2, 3]
print(obj2.other)  # Output: [1, 2, 3]

obj2.other.append(4)
print(obj1.other)  # Output: [1, 2, 3]
print(obj2.other)  # Output: [1, 2, 3, 4]
