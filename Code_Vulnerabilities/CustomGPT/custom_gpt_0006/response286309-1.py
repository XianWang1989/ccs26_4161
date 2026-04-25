
import pickle

class MyClass:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def __reduce__(self):
        return (self.__class__, (self.name, self.data), self.__getstate__())

    def __getstate__(self):
        return {'name': self.name, 'data': self.data}

    def __setstate__(self, state):
        self.name = state['name']
        self.data = state['data']

    def __deepcopy__(self, memo):
        if id(self) in memo:
            return memo[id(self)]
        # Use pickle for deepcopy
        result = pickle.loads(pickle.dumps(self))
        memo[id(self)] = result
        return result

# Example usage
if __name__ == "__main__":
    obj1 = MyClass("example", [1, 2, 3])
    obj2 = obj1.__deepcopy__({})

    print(f"Original: {obj1.name}, {obj1.data}")
    print(f"Copied: {obj2.name}, {obj2.data}")

    obj2.data.append(4)
    print(f"Modified Copied: {obj2.data}")
    print(f"Original after modifying copy: {obj1.data}")  # Should remain unchanged
