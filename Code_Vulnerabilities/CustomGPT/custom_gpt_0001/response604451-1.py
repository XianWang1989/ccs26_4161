
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Retrieve strings and their enable settings
search_strings = {
    'string1': config.get('SectionName', 'string1_enable'),
    'string2': config.get('SectionName', 'string2_enable'),
    'string3': config.get('SectionName', 'string3_enable'),
}

# Filter enabled search strings
enabled_strings = [key for key, value in search_strings.items() if value == 'yes']

# Telnet connection setup
tn = telnetlib.Telnet('hostname')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform the action here
        print("Found one of the enabled strings!")
