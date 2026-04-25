
import pickle

class MyClass:
    def __init__(self, value):
        self.value = value

    def __reduce__(self):
        return (self.__class__, (self.value,))

    def __getstate__(self):
        # Return state information for pickling
        return self.value

    def __setstate__(self, state):
        # Restore state information from unpickling
        self.value = state

    def __deepcopy__(self, memo):
        if id(self) in memo:
            return memo[id(self)]

        # Use pickle for deep copy
        result = pickle.loads(pickle.dumps(self, protocol=pickle.HIGHEST_PROTOCOL))
        memo[id(self)] = result
        return result
