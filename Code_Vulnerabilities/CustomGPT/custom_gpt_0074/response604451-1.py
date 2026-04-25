
import ConfigParser
import telnetlib

# Read configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Define your strings and their corresponding enable flags
search_strings = [
    ("string1", config.get('DEFAULT', 'string1_enable')),
    ("string2", config.get('DEFAULT', 'string2_enable')),
    ("string3", config.get('DEFAULT', 'string3_enable')),
]

# Start Telnet connection
tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()

    # Build the list of active strings based on config enable flags
    active_strings = [string for string, enabled in search_strings if enabled == "yes"]

    # Check if any of the active strings are in the received data
    if any(x in r for x in active_strings):
        # Perform your action here
        print("Match found in received data!")
