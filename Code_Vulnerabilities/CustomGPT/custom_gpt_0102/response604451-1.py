
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# List of strings and their enable flags
strings_to_check = [
    ("string1", config.get('SectionName', 'string1_enable')),
    ("string2", config.get('SectionName', 'string2_enable')),
    ("string3", config.get('SectionName', 'string3_enable')),
]

# Telnet setup
tn = telnetlib.Telnet('hostname', port)

while True:
    r = tn.read_some()

    # Create a list of enabled strings
    enabled_strings = [s for s, enabled in strings_to_check if enabled == "yes"]

    # Check if any enabled strings are present in the response
    if any(x in r for x in enabled_strings):
        # Perform the desired action
        print("Match found!")
