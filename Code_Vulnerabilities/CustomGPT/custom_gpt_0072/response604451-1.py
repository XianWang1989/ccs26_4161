
import ConfigParser
import telnetlib

# Initialize the config parser
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Set up your strings and their corresponding enable flags
search_strings = [
    (config.get('DEFAULT', 'string1'), config.get('DEFAULT', 'string1_enable')),
    (config.get('DEFAULT', 'string2'), config.get('DEFAULT', 'string2_enable')),
    (config.get('DEFAULT', 'string3'), config.get('DEFAULT', 'string3_enable')),
    # Add more strings as needed
]

tn = telnetlib.Telnet('your_telnet_server')

while True:
    r = tn.read_some()
    # Generate a list of enabled strings based on the config
    enabled_strings = [s for s, enabled in search_strings if enabled == 'yes']

    # Check if any of the enabled strings are in the response
    if any(s in r for s in enabled_strings):
        # Perform your action here
        print("Matching string found!")
