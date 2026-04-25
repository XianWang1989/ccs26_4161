
import ConfigParser

# Load your configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Define your strings and their enable flags
strings = {
    'string1': config.get('DEFAULT', 'string1'),
    'string1_enable': config.get('DEFAULT', 'string1_enable'),
    'string2': config.get('DEFAULT', 'string2'),
    'string2_enable': config.get('DEFAULT', 'string2_enable'),
    'string3': config.get('DEFAULT', 'string3'),
    'string3_enable': config.get('DEFAULT', 'string3_enable'),
}

# Construct a dynamic list of active strings
active_strings = [
    strings[key] for key in strings if key.endswith('_enable') and strings[key] == 'yes'
]

while True:
    r = tn.read_some()
    if any(x in r for x in active_strings):
        # Perform your action here
        action()
