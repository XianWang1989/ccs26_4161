
import ConfigParser
import telnetlib

# Load your configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Fetch strings and their enabled status from the config
string1 = 'your_first_string'
string2 = 'your_second_string'
string3 = 'your_third_string'

# Checking if the strings are enabled in the configuration
enabled_strings = []
if config.get('section_name', 'string1_enable') == 'yes':
    enabled_strings.append(string1)
if config.get('section_name', 'string2_enable') == 'yes':
    enabled_strings.append(string2)
if config.get('section_name', 'string3_enable') == 'yes':
    enabled_strings.append(string3)

# Connect using telnet
tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Implement the action you want to take when a match is found
        print("Match found!")
        # You can add more logic here based on which string was found if needed
