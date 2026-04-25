
import ConfigParser
import telnetlib

# Load your configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Define your strings and their corresponding configuration keys
search_strings = {
    "string1": config.get('DEFAULT', 'string1_enable'),  # Assumes strings are in a section called DEFAULT
    "string2": config.get('DEFAULT', 'string2_enable'),
    "string3": config.get('DEFAULT', 'string3_enable'),
}

# This will hold the strings that are enabled
enabled_strings = [key for key, value in search_strings.items() if value == "yes"]

tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()

    # Check if any of the enabled strings are in the response
    if any(x in r for x in enabled_strings):
        # Perform your action here
        action()  # Replace with the actual action you want to perform
