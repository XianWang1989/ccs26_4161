
import copy
import pickle

class CustomObject:
    def __deepcopy__(self, memo):
        # Use pickle to create a deep copy
        return pickle.loads(pickle.dumps(self, protocol=pickle.HIGHEST_PROTOCOL))

    def __getstate__(self):
        # Define what to pickle
        return self.__dict__

    def __setstate__(self, state):
        # Restore state
        self.__dict__.update(state)

# Example usage
if __name__ == "__main__":
    obj1 = CustomObject()
    obj1.attribute = "Original"

    # Create a deepcopy
    obj2 = copy.deepcopy(obj1)

    # Modify the original object
    obj1.attribute = "Modified"

    print(f"Original Attribute: {obj1.attribute}")  # Output: Modified
    print(f"Copied Attribute: {obj2.attribute}")    # Output: Original
