
import copy
import pickle

class CustomClass:
    def __init__(self, data):
        self.data = data

    def __reduce__(self):
        return (self.__class__.kwargs_new, (self.data,))

    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getstate__(self):
        return {'data': self.data}

    def __setstate__(self, state):
        self.data = state['data']

    def __deepcopy__(self, memo, options=None):
        # Use pickling to create a deepcopy
        new = pickle.loads(pickle.dumps(self, protocol=pickle.HIGHEST_PROTOCOL))

        # Implement custom options handling if needed
        if options and 'modify' in options:
            new.data += options['modify']

        memo[id(self)] = new
        return new

# Example usage
original = CustomClass(10)
options = {'modify': 5}
deep_copied = copy.deepcopy(original, options=options)

print(f"Original data: {original.data}")  # Output: 10
print(f"Deep copied data: {deep_copied.data}")  # Output: 15
