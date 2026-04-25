
import copy
import pickle

class CustomObject:
    def __init__(self, data):
        self.data = data

    def __reduce__(self):
        return (self.__class__, (self.data,), self.__getstate__())

    def __getstate__(self):
        return {'data': self.data}

    def __setstate__(self, state):
        self.data = state['data']

    def __deepcopy__(self, memo):
        # Use pickle to create a deep copy
        if id(self) in memo:
            return memo[id(self)]
        new, args, state = self.__reduce__()  # Get the new instance and arguments
        result = new(*args)  # Create the new instance
        if state:
            result.__setstate__(state)
        memo[id(self)] = result  # Add to memo
        return result
