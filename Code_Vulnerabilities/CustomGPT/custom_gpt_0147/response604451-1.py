
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Preparing a list of strings based on enabled status
strings_to_search = []

# Assuming strings are named uniformly like string1, string2, etc.
for i in range(1, 4):  # Change range(1, 4) based on number of strings you have
    string_name = 'string{}'.format(i)
    enable_key = '{}_enable'.format(string_name)

    if config.get('DEFAULT', enable_key) == 'yes':
        strings_to_search.append(config.get('DEFAULT', string_name))

# Assuming tn is already defined and connected
while True:
    r = tn.read_some()
    if any(x in r for x in strings_to_search):
        # Perform your action here
        action
