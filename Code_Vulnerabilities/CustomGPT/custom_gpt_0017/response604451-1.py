
import ConfigParser
import telnetlib

# Read configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

string1 = "example1"
string2 = "example2"
string3 = "example3"

# Check enabled status from config
strings_to_search = []
if config.get('Settings', 'string1_enable') == 'yes':
    strings_to_search.append(string1)
if config.get('Settings', 'string2_enable') == 'yes':
    strings_to_search.append(string2)
if config.get('Settings', 'string3_enable') == 'yes':
    strings_to_search.append(string3)

# Create telnet connection
tn = telnetlib.Telnet('your_telnet_server')

while True:
    r = tn.read_some()
    if any(x in r for x in strings_to_search):
        # Perform your action here
        print("Match found!")
