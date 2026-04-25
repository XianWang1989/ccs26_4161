
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize the Telnet connection (replace with your server details)
tn = telnetlib.Telnet('your.telnet.server')

# Gather enabled strings
search_strings = []
for i in range(1, 4):  # Assuming you have three strings
    enable_key = f"string{i}_enable"
    str_key = f"string{i}"

    if config.get('settings', enable_key) == 'yes':
        search_strings.append(config.get('settings', str_key))

# Main loop to read from Telnet
while True:
    r = tn.read_some()
    if any(x in r for x in search_strings):
        # Perform your action here
        print("Match found!")
