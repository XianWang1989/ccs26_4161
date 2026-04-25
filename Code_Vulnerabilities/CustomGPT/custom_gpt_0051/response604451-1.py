
import ConfigParser
import telnetlib

# Load the configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Define the strings and their enabled states
strings = [
    'string1', 'string2', 'string3'  # Add all your strings here
]
enabled_strings = [s for s in strings if config.get('Settings', f'{s}_enable') == 'yes']

tn = telnetlib.Telnet('your_telnet_host')  # Replace with your actual host

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Match found!")
