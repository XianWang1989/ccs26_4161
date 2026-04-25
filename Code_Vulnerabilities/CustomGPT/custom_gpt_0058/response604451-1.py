
import ConfigParser
import telnetlib

# Load configuration from config.ini
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Create a list of strings to search with their enabled states
search_strings = {
    "string1": config.get("DEFAULT", "string1_enable") == "yes",
    "string2": config.get("DEFAULT", "string2_enable") == "yes",
    "string3": config.get("DEFAULT", "string3_enable") == "yes",
}

while True:
    r = tn.read_some()
    # Filter only the enabled strings
    enabled_strings = [s for s, enabled in search_strings.items() if enabled]

    if any(x in r for x in enabled_strings):
        # Replace 'action' with the operation you want to perform
        action
