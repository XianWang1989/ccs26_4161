
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Assuming your config.ini looks something like this:
# [Settings]
# string1_enable = yes
# string2_enable = no
# string3_enable = yes

# Initialize the Telnet connection
tn = telnetlib.Telnet('your.telnet.server')

# Prepare the list of strings based on enabled settings
enabled_strings = []
if config.get('Settings', 'string1_enable') == 'yes':
    enabled_strings.append('string1')
if config.get('Settings', 'string2_enable') == 'yes':
    enabled_strings.append('string2')
if config.get('Settings', 'string3_enable') == 'yes':
    enabled_strings.append('string3')

while True:
    r = tn.read_some()
    # Check if any of the enabled strings are in the output
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Match found with strings:", enabled_strings)
