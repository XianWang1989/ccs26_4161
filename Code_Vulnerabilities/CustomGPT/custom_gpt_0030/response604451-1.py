
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Establish Telnet connection
tn = telnetlib.Telnet('your_telnet_host')

# Define strings and their enabled status from the config
strings_to_check = {
    'string1': config.get('SectionName', 'string1_enable'),
    'string2': config.get('SectionName', 'string2_enable'),
    'string3': config.get('SectionName', 'string3_enable'),
}

while True:
    r = tn.read_some()

    # Create a list of strings that are enabled
    enabled_strings = [s for s, enabled in strings_to_check.items() if enabled.lower() == 'yes']

    # Check for the presence of enabled strings in the received data
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Found one of the enabled strings!")
