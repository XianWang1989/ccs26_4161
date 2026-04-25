
def get_user_setting():
    # Your functions to retrieve settings
    return (foo(), bar(), baz())

def retrieve_setting():
    # Use next with a generator to get the first truthy result
    return next((setting for setting in get_user_setting() if setting), None)

# Example usage
setting = retrieve_setting()
