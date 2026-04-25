
def get_preferred_setting():
    settings_sources = [foo, bar, baz]  # List of functions to retrieve settings

    return next((setting for function in settings_sources if (setting := function())), None)

# Usage
result = get_preferred_setting()
