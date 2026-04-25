
import subprocess

def nmap_device_type(ip_address):
    """Use Nmap to get device type based on IP address."""
    result = subprocess.run(
        ["nmap", "-sP", ip_address],
        capture_output=True,
        text=True
    )
    return result.stdout

# Example IP address
ip_address = "192.168.1.1"
output = nmap_device_type(ip_address)
print(output)
