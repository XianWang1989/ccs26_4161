
import ConfigParser
import telnetlib

# Load configuration from config.ini
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize the telnet connection
tn = telnetlib.Telnet('hostname')  # Replace 'hostname' with your telnet server

# List of strings to search
search_strings = ['string1', 'string2', 'string3']
enabled_strings = []

# Collect enabled strings based on the config
for string in search_strings:
    enable_key = f"{string}_enable"
    if config.get('DEFAULT', enable_key) == 'yes':
        enabled_strings.append(string)

# Start reading from telnet
while True:
    r = tn.read_some()
    # Check if any enabled string is in the response
    if any(x in r for x in enabled_strings):
        # Perform the action if a match is found
        print("Action triggered for:", [x for x in enabled_strings if x in r])
