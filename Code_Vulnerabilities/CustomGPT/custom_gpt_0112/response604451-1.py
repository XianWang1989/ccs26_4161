
import telnetlib
import ConfigParser

# Load your configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize telnet
tn = telnetlib.Telnet('hostname', port)

# Define your strings and their corresponding enable flags
strings_to_search = {
    'string1': config.get('SectionName', 'string1_enable'),
    'string2': config.get('SectionName', 'string2_enable'),
    'string3': config.get('SectionName', 'string3_enable'),
}

# Convert the strings to search based on their enable flags
enabled_strings = [s for s, enabled in strings_to_search.items() if enabled.lower() == 'yes']

while True:
    r = tn.read_some()

    # Check if any enabled string is in the response
    if any(x in r for x in enabled_strings):
        # Take action if any string is found
        print("Matched one of the enabled strings!")
        # Add your action here
