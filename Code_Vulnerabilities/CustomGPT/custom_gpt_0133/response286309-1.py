
import copy

class CustomClass:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def kwargs_new(cls, new_kwargs, *new_args):
        retval = cls.__new__(cls, *new_args, **new_kwargs)
        retval.__init__(*new_args, **new_kwargs)
        return retval

    def __getstate__(self):
        # Customize what state to return for pickling
        return {'value': self.value}

    def __setstate__(self, state):
        # Restore state from the unpickled state
        self.value = state['value']

    def __getnewargs_ex__(self):
        return ((), {})

    def __reduce__(self):
        return (type(self).kwargs_new,
                (type(self), {}),  # new_kwargs are empty in this example
                self.__getstate__())

    def __deepcopy__(self, memo, **options):
        # Add your custom logic based on options here
        if 'include_value' in options and not options['include_value']:
            # If we don't want to include value, create an empty instance
            result = CustomClass(None)
        else:
            new, args, state = self.__reduce__()
            result = new(*args)
            result.__setstate__(state)

        memo[id(self)] = result
        return result

# Example usage of CustomClass and deepcopy
if __name__ == "__main__":
    obj = CustomClass(42)

    # Performing a deep copy including the value
    deep_copied_obj = copy.deepcopy(obj)
    print(f"Original value: {obj.value}, Deep copied value: {deep_copied_obj.value}")

    # Performing a deep copy excluding the value
    deep_copied_obj_exclude = copy.deepcopy(obj, include_value=False)
    print(f"Original value: {obj.value}, Deep copied value (excluded): {deep_copied_obj_exclude.value}")
