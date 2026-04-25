
from getmac import get_mac_address
import requests

def is_wireless_mac(mac):
    """Check if a MAC address corresponds to a wireless network interface."""
    # Define common OUI patterns for wireless devices (this list can be expanded)
    wireless_ouis = [
        "00:1A:2B",  # Example OUI for wireless
        "00:1C:BF",  # Example OUI for wireless
        "00:24:6C",  # Example OUI for wireless
        # (Add more known wireless OUI here)
    ]

    # Get the first three octets from the MAC address
    mac_prefix = mac.upper()[:8]

    # Check against known wireless OUIs
    return mac_prefix in wireless_ouis

def main():
    # Example MAC address to check
    mac_address = "00:1A:2B:3C:4D:5E"  # Replace with your MAC address

    if is_wireless_mac(mac_address):
        print(f"The MAC address {mac_address} is likely for a wireless card.")
    else:
        print(f"The MAC address {mac_address} is likely for an Ethernet card or unknown.")

if __name__ == "__main__":
    main()
