
import pickle

class MyClass:
    def __init__(self, data):
        self.data = data

    def __reduce__(self):
        return (type(self), (self.data,))

    def __deepcopy__(self, memo, options=None):
        if id(self) in memo:
            return memo[id(self)]

        # Use pickle to create a deep copy
        result = pickle.loads(pickle.dumps(self, protocol=pickle.HIGHEST_PROTOCOL))

        # Optionally modify the result based on `options`
        if options and 'transform' in options:
            result.data = options['transform'](result.data)

        memo[id(self)] = result
        return result

# Example usage
original = MyClass([1, 2, 3])
options = {'transform': lambda x: [i * 2 for i in x]}  # Option to double the values
copy = original.__deepcopy__({}, options)

print("Original data:", original.data)  # Output: [1, 2, 3]
print("Copied data:", copy.data)        # Output: [2, 4, 6]
