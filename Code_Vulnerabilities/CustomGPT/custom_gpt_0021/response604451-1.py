
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read("config.ini")

# Initialize telnet connection
tn = telnetlib.Telnet('hostname', port)

# List of strings you want to search for
search_strings = [string1, string2, string3]  # Add more as needed
enabled_strings = []

# Populate enabled strings based on config
for idx, string in enumerate(search_strings):
    if config.get('DEFAULT', f'string{idx + 1}_enable') == 'yes':
        enabled_strings.append(string)

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Match found!")
