
def __deepcopy__(self, memo, custom_option=None):
    new, args, state = self.__reduce__()
    result = new(*args)
    if state:
        result.__setstate__(state)

    # Example of using custom_option
    if custom_option:
        # modify result based on custom_option logic
        pass  # Add your custom behavior here

    memo[id(self)] = result
    return result
