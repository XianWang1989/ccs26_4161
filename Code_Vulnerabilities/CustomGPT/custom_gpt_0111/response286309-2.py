
def __deepcopy__(self, memo, custom_options=None):
    new, args, state = self.__reduce__()
    result = new(*args)
    if state:
        result.__setstate__(state)

    if custom_options:
        # Handle options (e.g., selectively copying attributes)
        for key in custom_options.get('attributes', []):
            if hasattr(self, key):
                setattr(result, key, copy.deepcopy(getattr(self, key), memo))

    memo[id(self)] = result
    return result
