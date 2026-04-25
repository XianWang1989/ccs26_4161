
import netifaces
import getmac

def get_interface_type(mac_address):
    # Predefined list of OUIs for common wireless manufacturers
    wireless_ouedian = ["00:1A:11", "00:1E:4F", "00:08:9B", "78:2B:CB", "A0:36:9F"]  # Add more as needed

    # Check if the MAC address starts with known wireless OUI
    for oui in wireless_ouedian:
        if mac_address.startswith(oui):
            return "Wireless Card"

    return "Ethernet Card"

def classify_network_interfaces():
    interfaces = netifaces.interfaces()
    interface_info = {}

    for interface in interfaces:
        try:
            mac = getmac.get_mac_address(interface=interface)
            if mac:
                interface_info[interface] = get_interface_type(mac)
        except Exception as e:
            interface_info[interface] = str(e)

    return interface_info

if __name__ == "__main__":
    interface_classification = classify_network_interfaces()
    for interface, interface_type in interface_classification.items():
        print(f"{interface}: {interface_type}")
