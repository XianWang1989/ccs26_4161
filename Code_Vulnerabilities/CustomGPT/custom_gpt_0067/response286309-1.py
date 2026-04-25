
import copy
import pickle

class MyBaseClass:
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
        return (type(self).kwargs_new,
                (type(self), new_kwargs) + tuple(new_args),
                state)

class MyClass(MyBaseClass):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __deepcopy__(self, memo):
        # Use pickling and unpickling for deep copying
        if id(self) in memo:
            return memo[id(self)]
        new_self = pickle.loads(pickle.dumps(self))
        memo[id(self)] = new_self
        return new_self

# Usage Example
obj1 = MyClass("test", 42)
obj2 = copy.deepcopy(obj1)

print(obj1.name, obj1.value)  # Output: test 42
print(obj2.name, obj2.value)  # Output: test 42
obj2.name = "changed"
print(obj1.name)  # Output: test
print(obj2.name)  # Output: changed
