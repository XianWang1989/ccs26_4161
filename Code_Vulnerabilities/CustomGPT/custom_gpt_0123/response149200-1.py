
import subprocess
import re

# List of known wireless OUI prefixes (partial list)
wireless_ouis = {
    '00:1A:22': 'Wireless',
    '00:1E:4F': 'Wireless',
    '00:25:64': 'Wireless',
    '00:14:51': 'Wireless',
    '00:18:4D': 'Wireless',
    # Add more known wireless OUIs as needed
}

def get_mac_type(mac_address):
    # Normalize the MAC address format
    mac_address = mac_address.upper()

    # Check if MAC address belongs to known wireless OUI
    for oui in wireless_ouis:
        if mac_address.startswith(oui):
            return 'Wireless'

    # If the MAC does not match any wireless OUIs, assume Ethernet or unknown
    return 'Ethernet or Unknown'

def get_mac_addresses():
    # Use arp command to get MAC addresses from the network
    result = subprocess.run(['arp', '-a'], capture_output=True, text=True)
    return result.stdout

def main():
    output = get_mac_addresses()
    mac_addresses = re.findall(r'..:..:..:..:..:..', output)

    for mac in mac_addresses:
        mac_type = get_mac_type(mac)
        print(f'MAC Address: {mac} - Type: {mac_type}')

if __name__ == "__main__":
    main()
