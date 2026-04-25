
def __deepcopy__(self, memo, options=None):
    # You can use options to modify copying behavior
    new, args, state = self.__reduce__()
    result = new(*args)
    if state:
        result.__setstate__(state)
    memo[id(self)] = result
    return result
