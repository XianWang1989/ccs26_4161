
import ConfigParser
import telnetlib

# Load your configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Define your strings and their enable/disable flags
strings = {
    "string1": config.get("settings", "string1_enable"),
    "string2": config.get("settings", "string2_enable"),
    "string3": config.get("settings", "string3_enable"),
}

# Prepare a list of enabled strings
enabled_strings = [key for key, value in strings.items() if value == "yes"]

# Telnet connection setup (assuming tn is already established)
while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Match found!")
