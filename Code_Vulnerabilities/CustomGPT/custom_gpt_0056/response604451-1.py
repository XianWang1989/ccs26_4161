
import telnetlib
import ConfigParser

# Read configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

string1 = "string1"
string2 = "string2"
string3 = "string3"

# Create a list of strings based on the enabled settings
enabled_strings = []

if config.get('Settings', 'string1_enable') == "yes":
    enabled_strings.append(string1)
if config.get('Settings', 'string2_enable') == "yes":
    enabled_strings.append(string2)
if config.get('Settings', 'string3_enable') == "yes":
    enabled_strings.append(string3)

# Telnet connection
tn = telnetlib.Telnet('hostname', port)

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform the desired action here
        print("Found a match!")

# Remember to close the telnet connection when done.
tn.close()
