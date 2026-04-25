
import ConfigParser
import telnetlib

# Read the config file
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Example strings with enable flags
search_strings = [
    (config.get('SectionName', 'string1'), config.get('SectionName', 'string1_enable')),
    (config.get('SectionName', 'string2'), config.get('SectionName', 'string2_enable')),
    (config.get('SectionName', 'string3'), config.get('SectionName', 'string3_enable')),
    # Add more strings as needed
]

while True:
    r = tn.read_some()

    # Filter enabled strings
    enabled_strings = [s for s, enabled in search_strings if enabled.lower() == 'yes']

    # Check if any of the enabled strings are in the response
    if any(s in r for s in enabled_strings):
        # Perform your action here
        print("Match found! Performing action...")
