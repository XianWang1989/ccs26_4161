
import telnetlib
import ConfigParser

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Telnet connection setup
tn = telnetlib.Telnet('your_telnet_host')

# Define strings and their enable statuses
strings = [
    (config.get('SectionName', 'string1'), config.get('SectionName', 'string1_enable')),
    (config.get('SectionName', 'string2'), config.get('SectionName', 'string2_enable')),
    (config.get('SectionName', 'string3'), config.get('SectionName', 'string3_enable')),
    # Add more strings as needed
]

while True:
    r = tn.read_some()

    # Filter strings based on enable status
    active_strings = [s for s, enabled in strings if enabled.lower() == 'yes']

    # Check if any of the active strings are in the response
    if any(x in r for x in active_strings):
        # Your action here
        print("Match found!")

# Remember to handle exceptions and proper telnet operations as needed.
