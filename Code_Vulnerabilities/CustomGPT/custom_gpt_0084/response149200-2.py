
import subprocess

def get_device_info(ip_address):
    result = subprocess.run(['nmap', '-sP', ip_address], capture_output=True, text=True)
    return result.stdout

# Example usage
ip_address = '192.168.1.1'  # Replace with actual IP address
info = get_device_info(ip_address)
print(info)
