
import configparser
import telnetlib

# Load configurations from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# Define the strings and their corresponding config variables
strings = ['string1', 'string2', 'string3']
enabled_strings = []

# Check which strings are enabled
for s in strings:
    if config.get('DEFAULT', f'{s}_enable') == 'yes':
        enabled_strings.append(s)

# Telnet connection (make sure to replace 'hostname' and 'port' with actual values)
tn = telnetlib.Telnet('hostname', port)

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your desired action here
        print("Match found! Performing action...")
