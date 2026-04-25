
import pickle

class MyClass:
    def __init__(self, data):
        self.data = data

    def __reduce__(self):
        return (self.__class__.kwargs_new,
                (self.data,),
                self.__getstate__())

    @staticmethod
    def kwargs_new(cls, *args, **kwargs):
        instance = cls.__new__(cls)
        instance.__init__(*args, **kwargs)
        return instance

    def __getstate__(self):
        return {'data': self.data}

    def __setstate__(self, state):
        self.data = state['data']

    def __deepcopy__(self, memo):
        # Using pickle to deep copy the object
        new_obj = pickle.loads(pickle.dumps(self, protocol=pickle.HIGHEST_PROTOCOL))
        memo[id(self)] = new_obj
        return new_obj

# Usage example
if __name__ == "__main__":
    original = MyClass([1, 2, 3])
    copy_instance = original.__deepcopy__({})

    print("Original data:", original.data)
    print("Copied data:", copy_instance.data)

    # Modify the copy
    copy_instance.data.append(4)

    print("After modification:")
    print("Original data:", original.data)
    print("Copied data:", copy_instance.data)
