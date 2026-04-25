
import telnetlib
import ConfigParser

# Read configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize the Telnet connection
tn = telnetlib.Telnet('your_telnet_host')

# Prepare the strings and their enablement status
search_strings = {
    config.get('Settings', 'string1'): config.get('Settings', 'string1_enable'),
    config.get('Settings', 'string2'): config.get('Settings', 'string2_enable'),
    config.get('Settings', 'string3'): config.get('Settings', 'string3_enable'),
}

# Create a list of enabled search strings
enabled_search_strings = [string for string, enabled in search_strings.items() if enabled == "yes"]

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_search_strings):
        # Place your action here
        print("Found a match!")
        # action

# Don't forget to close the connection if needed
# tn.close()
