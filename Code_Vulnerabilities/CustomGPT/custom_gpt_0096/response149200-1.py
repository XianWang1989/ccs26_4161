
import requests

def get_mac_info(mac):
    # Fetch MAC address info from a public API
    url = f"https://api.macaddress.io/v1?apiKey=YOUR_API_KEY&output=json&search={mac}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data.get('vendorDetails', {}).get('companyName'), data.get('vendorDetails', {}).get('type')
    else:
        print("Error fetching data.")
        return None, None

def classify_mac(mac):
    company, type = get_mac_info(mac)
    if company:
        if 'wireless' in type.lower():
            return 'Wireless Card'
        elif 'ethernet' in type.lower():
            return 'Ethernet Card'
        else:
            return 'Unknown Type'
    return 'No Data Available'

mac_address = '00:1A:2B:3C:4D:5E'  # Example MAC address
card_type = classify_mac(mac_address)
print(f"The MAC address {mac_address} is associated with a: {card_type}")
