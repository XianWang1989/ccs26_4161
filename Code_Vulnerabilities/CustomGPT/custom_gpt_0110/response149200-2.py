
import maclookup

def get_mac_type(mac_address):
    data = maclookup.lookup(mac_address)
    if "wireless" in data.get("category", "").lower():
        return "Wireless Card"
    elif "ethernet" in data.get("category", "").lower():
        return "Ethernet Card"
    return "Unknown type"
