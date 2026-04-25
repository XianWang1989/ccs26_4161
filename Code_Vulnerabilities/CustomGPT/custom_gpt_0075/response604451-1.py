
import telnetlib
import ConfigParser

# Load config
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize the telnet connection
tn = telnetlib.Telnet('your_telnet_host')

# List of strings to check
strings_to_check = ['string1', 'string2', 'string3']
enabled_strings = []

# Gather enabled strings based on config
for s in strings_to_check:
    if config.get(s + '_enable', fallback='no') == 'yes':
        enabled_strings.append(s)

# Run the search loop
while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform the desired action
        print("Action triggered based on found strings.")
