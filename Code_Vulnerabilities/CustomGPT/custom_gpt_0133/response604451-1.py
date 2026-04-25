
import ConfigParser
import telnetlib

# Read configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize your strings and their enable status
search_strings = {
    'string1': config.get('Settings', 'string1_enable') == "yes",
    'string2': config.get('Settings', 'string2_enable') == "yes",
    'string3': config.get('Settings', 'string3_enable') == "yes",
}

# Prepare a list of active search strings
active_search_strings = [s for s, enabled in search_strings.items() if enabled]

# Set up the Telnet connection
tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()

    # Check for any active search strings in the received data
    if any(x in r for x in active_search_strings):
        # Perform your action here
        print("Match found!")
