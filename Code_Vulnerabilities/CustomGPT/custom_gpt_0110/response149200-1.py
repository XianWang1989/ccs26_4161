
import requests

# Predefined OUIs for demonstration purposes
# In a real situation, you would fetch this from a complete OUI list
# You can find OUI lists in databases or online, such as IEEE or vendor websites
wireless_ouis = {
    '00:1A:11', '00:1B:22', '00:1C:33',  # Example wireless OUIs
}
ethernet_ouis = {
    '00:1D:44', '00:1E:55', '00:1F:66',  # Example Ethernet OUIs
}

def get_mac_type(mac_address):
    try:
        # Normalize MAC address format
        mac_prefix = mac_address.upper()[:8]  # Get first 8 characters (e.g., '00:1A:11')

        if mac_prefix in wireless_ouis:
            return "Wireless Card"
        elif mac_prefix in ethernet_ouis:
            return "Ethernet Card"
        else:
            return "Unknown type"
    except Exception as e:
        return str(e)

# Example usage
mac_address = "00:1A:11:FF:EE:DD"
device_type = get_mac_type(mac_address)
print(f"The device with MAC address {mac_address} is a {device_type}.")
