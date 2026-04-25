
import telnetlib
import ConfigParser

# Load your config
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Retrieve your enable flags and strings
strings = {
    'string1': config.get('DEFAULT', 'string1'),
    'string2': config.get('DEFAULT', 'string2'),
    'string3': config.get('DEFAULT', 'string3')
}

enabled = {
    'string1': config.get('DEFAULT', 'string1_enable') == 'yes',
    'string2': config.get('DEFAULT', 'string2_enable') == 'yes',
    'string3': config.get('DEFAULT', 'string3_enable') == 'yes'
}

# Establish a telnet connection (change to your parameters)
tn = telnetlib.Telnet('your_telnet_host', your_telnet_port)

while True:
    r = tn.read_some()

    # Collect all enabled strings for the search
    search_strings = [s for s, is_enabled in enabled.items() if is_enabled]

    # Check if any of the enabled strings are in the response
    if any(x in r for x in search_strings):
        # Perform the desired action
        print("One of the enabled strings was found!")
        # Add your action here

