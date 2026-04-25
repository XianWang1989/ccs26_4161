
import copy

class CustomClass:
    def __init__(self, value, decoy=None):
        self.value = value
        self.decoy = decoy or []

    def __deepcopy__(self, memo, options=None):
        # If options is None, initialize it to an empty dictionary
        options = options or {}

        # Custom behavior based on options
        if options.get('copy_decoy', True):
            # Deepcopy decoy attribute
            new_decoy = copy.deepcopy(self.decoy, memo)
        else:
            # Reference the current decoy without deepcopying
            new_decoy = self.decoy

        # Create a new instance
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result

        # Copy the attributes
        result.value = copy.deepcopy(self.value, memo)
        result.decoy = new_decoy

        return result

# Example usage
original = CustomClass(value=42, decoy=[1, 2, 3])
deep_copied_with_options = copy.deepcopy(original, options={'copy_decoy': False})

print(original.value)  # Output: 42
print(original.decoy)  # Output: [1, 2, 3]

print(deep_copied_with_options.value)  # Output: 42
print(deep_copied_with_options.decoy)  # Output: [1, 2, 3] (same reference as original)
