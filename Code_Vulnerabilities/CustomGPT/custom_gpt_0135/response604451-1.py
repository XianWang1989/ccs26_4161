
import ConfigParser
import telnetlib

# Load configurations
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize telnet connection (assuming you have your host and port)
tn = telnetlib.Telnet('your_telnet_host', your_telnet_port)

# List of strings to search for
search_strings = [
    (config.get('Section', 'string1'), config.get('Section', 'string1_enable')),
    (config.get('Section', 'string2'), config.get('Section', 'string2_enable')),
    (config.get('Section', 'string3'), config.get('Section', 'string3_enable')),
]

while True:
    r = tn.read_some()

    # Filter enabled strings
    enabled_strings = [s for s, enabled in search_strings if enabled == 'yes']

    # Check if any enabled string is in the response
    if any(x in r for x in enabled_strings):
        # Your action here
        print("Found one of the enabled strings!")
