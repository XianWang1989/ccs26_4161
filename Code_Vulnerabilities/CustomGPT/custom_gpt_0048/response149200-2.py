
import subprocess

def scan_network(ip):
    try:
        result = subprocess.run(['nmap', '-sP', ip], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"Error scanning network: {e}")
        return None

# Example usage
output = scan_network("192.168.1.1")
print(output)
