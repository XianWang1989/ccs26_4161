
import ConfigParser
import telnetlib

# Example: Read your config.ini file
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Define your strings and their enabled states
strings = {
    'string1': config.get('Settings', 'string1_enable'),
    'string2': config.get('Settings', 'string2_enable'),
    'string3': config.get('Settings', 'string3_enable')
}

# Create a filter function to get enabled strings
enabled_strings = [s for s in strings if strings[s] == 'yes']

# Connect to your Telnet session
tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Place your action code here
        print("One of the enabled strings found!")
