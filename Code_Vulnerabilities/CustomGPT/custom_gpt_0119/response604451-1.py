
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Example strings and enabling from config
search_strings = []
if config.get('Settings', 'string1_enable') == 'yes':
    search_strings.append(config.get('Settings', 'string1'))
if config.get('Settings', 'string2_enable') == 'yes':
    search_strings.append(config.get('Settings', 'string2'))
if config.get('Settings', 'string3_enable') == 'yes':
    search_strings.append(config.get('Settings', 'string3'))

# Setup Telnet connection
tn = telnetlib.Telnet('your.telnethost.com')

while True:
    r = tn.read_some()
    if any(x in r for x in search_strings):
        # Perform the desired action
        print("Match found!")
