
import ConfigParser
import telnetlib

# Assuming you have already set up your telnet connection
tn = telnetlib.Telnet('host', port)

# Load configurations
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Create a dictionary to store strings and their enable status
strings_to_search = {
    'string1': config.get('section_name', 'string1_enable'),
    'string2': config.get('section_name', 'string2_enable'),
    'string3': config.get('section_name', 'string3_enable')
}

while True:
    r = tn.read_some()

    # Compile a list of enabled search strings
    enabled_search_strings = [string for string, enabled in strings_to_search.items() if enabled == "yes"]

    # Check if any of the enabled strings are in the received data
    if any(x in r for x in enabled_search_strings):
        action  # Perform your action here
