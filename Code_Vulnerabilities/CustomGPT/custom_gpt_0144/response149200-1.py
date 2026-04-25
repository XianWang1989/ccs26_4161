import psutil
import subprocess

def get_interface_type():
    interfaces = psutil.net_if_addrs()
    interface_types = {}

    for interface in interfaces:
        try:
            # Use iwconfig to check for wireless interfaces (Linux only)
            result = subprocess.run(['iwconfig', interface],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.DEVNULL,
                                    text=True)
            if 'no wireless extensions' not in result.stdout:
                interface_types[interface] = 'wireless'
            else:
                interface_types[interface] = 'ethernet'
        except Exception as e:
            interface_types[interface] = 'unknown'
    return interface_types

def get_mac_and_type():
    interface_info = psutil.net_if_addrs()
    interface_types = get_interface_type()

    for interface, addresses in interface_info.items():
        for addr in addresses:
            if addr.family == psutil.AF_LINK:
                print(f"Interface: {interface}, MAC: {addr.address}, Type: {interface_types.get(interface, 'unknown')}")

get_mac_and_type()
