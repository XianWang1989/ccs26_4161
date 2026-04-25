
import copy

class Base:
    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        """
        Override this method to use a different new.
        """
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getstate__(self):
        return {}

    def __setstate__(self, state):
        self.__dict__.update(state)

    def __getnewargs_ex__(self):
        return ((), {})

    def __reduce__(self):
        new_args, new_kwargs = self.__getnewargs_ex__()
        state = self.__getstate__()
        return (type(self).kwargs_new,
                (type(self), new_kwargs,) + tuple(new_args),
                state)


class CustomObject(Base):
    def __init__(self, data, metadata):
        self.data = data
        self.metadata = metadata

    def __deepcopy__(self, memo, options=None):
        new, args, state = self.__reduce__()
        result = new(*args)
        if state:
            result.__setstate__(state)

        # Store the result in memo to avoid recursion
        memo[id(self)] = result

        # Example of options handling
        if options and 'include_metadata' in options and not options['include_metadata']:
            result.metadata = None  # Don't copy metadata if requested

        return result

# Example usage
original = CustomObject(data=[1, 2, 3], metadata={'info': 'example'})
options = {'include_metadata': False}  # Example option to not copy metadata
copy_obj = copy.deepcopy(original, options=options)

print("Original:", original.data, original.metadata)
print("Copy:", copy_obj.data, copy_obj.metadata)  # Metadata should be None
