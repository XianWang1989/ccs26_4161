
import telnetlib
import ConfigParser

# Load your config
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize the telnet connection
tn = telnetlib.Telnet('your_telnet_host')

# Define your strings and their enable flags
search_strings = {
    'string1': config.get('SectionName', 'string1_enable'),
    'string2': config.get('SectionName', 'string2_enable'),
    'string3': config.get('SectionName', 'string3_enable'),
}

while True:
    r = tn.read_some()

    # Filter the strings based on their enable flags
    active_strings = [s for s, enabled in search_strings.items() if enabled == 'yes']

    # Check if any active string is present in the response
    if any(x in r for x in active_strings):
        # Perform your action here
        print("Matched one of the active strings!")
