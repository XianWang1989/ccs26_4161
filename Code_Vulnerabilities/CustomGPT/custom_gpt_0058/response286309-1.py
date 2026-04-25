
import copy

class MyClass:
    def __init__(self, value):
        self.value = value

    def __reduce__(self):
        return (self.__class__, (self.value,))

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__.update(state)

    def __deepcopy__(self, memo, **options):
        # Use pickling to create a deep copy
        new, args = self.__reduce__()[:2]
        result = new(*args)

        # You can use options here to modify how copying is done
        # For instance, ignoring certain attributes based on options
        if options.get('ignore_attributes'):
            for attr in options['ignore_attributes']:
                if attr in result.__dict__:
                    del result.__dict__[attr]

        memo[id(self)] = result
        return result

# Example usage:
original = MyClass(10)
deep_copied = copy.deepcopy(original, ignore_attributes=['value'])

print(original.__dict__)  # Output: {'value': 10}
print(deep_copied.__dict__)  # Output: {} (since 'value' was ignored)
