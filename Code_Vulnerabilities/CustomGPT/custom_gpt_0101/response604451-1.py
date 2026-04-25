
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config.ini')

enabled_strings = []

# Check which strings are enabled
for i in range(1, 4):  # Assuming you have string1, string2, string3
    if config.get('Section', f'string{i}_enable') == 'yes':
        enabled_strings.append(config.get('Section', f'string{i}'))

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
