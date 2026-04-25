
import subprocess
import re

def get_mac_vendor(mac):
    # Using nmap to get MAC address vendor info
    try:
        output = subprocess.check_output(['nmap', '-sn', '192.168.1.0/24']).decode('utf-8')
        for line in output.splitlines():
            if mac.lower() in line.lower():
                match = re.search(r'(\w\w:\w\w:\w\w)', line)
                if match:
                    return line
    except subprocess.CalledProcessError as e:
        print(f"Error running nmap: {e}")
    return None

def get_card_type(mac):
    vendor_info = get_mac_vendor(mac)
    if vendor_info:
        # Simple heuristics based on vendor (example only)
        if any(vendor in vendor_info for vendor in ['Apple', 'Dell', 'HP']):
            return 'Likely a Laptop (Wireless)'
        elif any(vendor in vendor_info for vendor in ['Cisco', 'Netgear']):
            return 'Likely a Wired Device (Ethernet)'
        else:
            return 'Unknown Type'
    return 'MAC not found in network scan'

# Example usage
mac_address = '00:1A:2B:3C:4D:5E'
card_type = get_card_type(mac_address)
print(f"MAC Address: {mac_address} - Card Type: {card_type}")
