
import ConfigParser
from telnetlib import Telnet

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Define the strings and their enabled states
strings_to_check = []
for i in range(1, 4):  # Assuming you have string1, string2, string3
    string_key = 'string{}_enable'.format(i)
    if config.get('YourSection', string_key) == "yes":
        strings_to_check.append(config.get('YourSection', 'string{}'.format(i)))

# Connect to Telnet
tn = Telnet('your_telnet_host')

while True:
    r = tn.read_some()

    # Check if any enabled string is in the read data
    if any(x in r for x in strings_to_check):
        # Perform your action here
        print("Found one of the enabled strings!")
