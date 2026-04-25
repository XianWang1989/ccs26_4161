
import pickle

class MyClass:
    # Example attributes
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def __deepcopy__(self, memo):
        # Perform a deep copy using the pickling method
        if id(self) in memo:
            return memo[id(self)]

        # Create a new instance using the `__reduce__` method
        new_instance = pickle.loads(pickle.dumps(self))
        memo[id(self)] = new_instance
        return new_instance

    # Example state management methods
    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__.update(state)

# Example Usage
original = MyClass(10, "Hello")
deep_copied = original.__deepcopy__({})

print(original.attr1, original.attr2)  # Output: 10 Hello
print(deep_copied.attr1, deep_copied.attr2)  # Output: 10 Hello

# Modifying the deep copy
deep_copied.attr1 = 20
print(original.attr1)  # Output: 10 (remains unchanged)
print(deep_copied.attr1)  # Output: 20
