
import ConfigParser
import telnetlib

# Load your config
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Telnet connection setup
tn = telnetlib.Telnet('hostname', port)

# Collect enabled strings
enabled_strings = []
for key in ['string1_enable', 'string2_enable', 'string3_enable']:
    if config.get('SectionName', key) == 'yes':
        string_name = key.replace('_enable', '')
        enabled_strings.append(config.get('SectionName', string_name))

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Match found!")
