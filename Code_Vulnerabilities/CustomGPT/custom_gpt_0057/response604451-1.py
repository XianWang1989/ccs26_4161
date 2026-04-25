
import telnetlib
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config.ini')

string_list = ['string1', 'string2', 'string3']
enabled_strings = [s for s in string_list if config.get(s, 'enable') == 'yes']

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Match found!")
