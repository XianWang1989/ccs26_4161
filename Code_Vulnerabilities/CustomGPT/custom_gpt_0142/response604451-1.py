
import telnetlib
import ConfigParser

# Load your configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Example strings
strings_config = {
    'string1': config.get('Section', 'string1_enable'),
    'string2': config.get('Section', 'string2_enable'),
    'string3': config.get('Section', 'string3_enable')
}

# Create a list of enabled strings
enabled_strings = [s for s, enabled in strings_config.items() if enabled == 'yes']

# Establish Telnet connection (e.g., to some server)
tn = telnetlib.Telnet('your_telnet_server', 23)

while True:
    r = tn.read_some()

    # Check if any enabled string is found in the response
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Found a match!")
