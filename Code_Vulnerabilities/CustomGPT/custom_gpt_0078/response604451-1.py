
import ConfigParser
import telnetlib

# Initialize ConfigParser
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Read the enabled strings from the config
enabled_strings = []
for i in range(1, 4):  # Assuming you have string1 to string3
    string_key = f"string{i}"
    enable_key = f"{string_key}_enable"
    if config.get('DEFAULT', enable_key) == 'yes':
        enabled_strings.append(config.get('DEFAULT', string_key))

# Start telnet session
tn = telnetlib.Telnet('your_host', your_port)

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Match found! Performing action.")
