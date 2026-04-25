
def get_user_setting():
    # Dummy functions for demonstration
    return foo(), bar(), baz()

# List of functions to check
check_functions = [foo, bar, baz]

# Get the first non-False result
result = next((func() for func in check_functions if func()), None)

return result
