
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Get enabled strings from config
strings = []
if config.get('Settings', 'string1_enable') == 'yes':
    strings.append(config.get('Settings', 'string1'))
if config.get('Settings', 'string2_enable') == 'yes':
    strings.append(config.get('Settings', 'string2'))
if config.get('Settings', 'string3_enable') == 'yes':
    strings.append(config.get('Settings', 'string3'))

# Your telnet connection
tn = telnetlib.Telnet('hostname')

while True:
    r = tn.read_some()
    if any(x in r for x in strings):
        # Your action here
        print("Match found!")
