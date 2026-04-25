
import ConfigParser
from telnetlib import Telnet

# Load the configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Define the strings and their corresponding enable statuses
strings = {
    'string1': config.get('SectionName', 'string1_enable'),
    'string2': config.get('SectionName', 'string2_enable'),
    'string3': config.get('SectionName', 'string3_enable'),
}

# Initialize Telnet connection
tn = Telnet('your.telnet.server')

while True:
    r = tn.read_some()

    # Create a list of enabled strings to search for
    search_strings = [key for key, value in strings.items() if value == "yes"]

    # Check if any of the enabled strings are in the response
    if any(x in r for x in search_strings):
        # Perform your action here
        print("Match found!")

# Close the connection when done
tn.close()
