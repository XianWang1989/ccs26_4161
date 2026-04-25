
import telnetlib
import ConfigParser

# Load configurations from config.ini
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Example strings
strings = ["string1", "string2", "string3"]
enabled_strings = []

# Check which strings are enabled
for s in strings:
    if config.get(s + "_enable") == "yes":
        enabled_strings.append(s)

# Telnet connection setup
tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("One of the enabled strings was found!")
