
import ConfigParser
import telnetlib

# Load the configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Set up your strings and their enable flags
strings = {
    'string1': config.get('SectionName', 'string1_enable'),
    'string2': config.get('SectionName', 'string2_enable'),
    'string3': config.get('SectionName', 'string3_enable'),
}

# Initialize your Telnet connection
tn = telnetlib.Telnet('your.telnet.server')

while True:
    r = tn.read_some()

    # Create a dynamic list of active strings to check
    active_strings = [key for key, value in strings.items() if value == 'yes']

    # Check if any of the active strings are in the response
    if any(x in r for x in active_strings):
        # Your action here
        print("Matched one of the enabled strings!")
