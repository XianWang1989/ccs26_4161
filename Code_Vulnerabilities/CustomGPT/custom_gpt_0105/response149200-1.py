
import requests

def get_mac_vendor(mac):
    """Get the vendor of a MAC address."""
    url = f"https://api.macvendors.com/{mac}"
    try:
        response = requests.get(url)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def identify_card_type(mac):
    """Identify if the network card is Ethernet or Wireless."""
    vendor = get_mac_vendor(mac)
    print(f"Vendor for MAC {mac}: {vendor}")

    wireless_vendors = ["Intel", "Broadcom", "Atheros", "Qualcomm", "Marvell"]
    ethernet_vendors = ["Realtek", "Marvell", "Intel"]

    # Basic identification logic
    if any(vendor.startswith(v) for v in wireless_vendors):
        return "Wireless Card"
    elif any(vendor.startswith(v) for v in ethernet_vendors):
        return "Ethernet Card"
    else:
        return "Unknown Card Type"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
card_type = identify_card_type(mac_address)
print(f"The card type for {mac_address} is: {card_type}")
