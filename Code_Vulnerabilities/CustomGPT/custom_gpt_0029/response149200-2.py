
import subprocess
import requests

def get_mac_info(mac_address):
    url = f"https://api.macvendors.com/{mac_address}"
    response = requests.get(url)

    return response.text if response.status_code == 200 else "MAC address not found."

def scan_network():
    result = subprocess.run(['nmap', '-sn', '192.168.1.0/24'], capture_output=True, text=True)
    return result.stdout

# Example usage
mac_address = "00:14:22:01:23:45"
vendor_info = get_mac_info(mac_address)
network_info = scan_network()

print("Vendor Info:", vendor_info)
print("Network Scan Results:\n", network_info)
