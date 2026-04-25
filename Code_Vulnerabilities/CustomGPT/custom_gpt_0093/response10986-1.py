
import requests

# A basic mapping of country codes to their default Accept-Language and Accept-Charset
country_language_mapping = {
    'US': {'language': 'en-US', 'charset': 'utf-8'},
    'RU': {'language': 'ru-RU', 'charset': 'windows-1251'},
    'FR': {'language': 'fr-FR', 'charset': 'utf-8'},
    # Add more countries as needed
}

def get_country_code(ip):
    """Get the country code based on IP address."""
    response = requests.get(f"https://ipapi.co/{ip}/json/")
    data = response.json()
    return data.get('country', None)

def get_default_headers(ip):
    """Get Accept-Language and Accept-Charset based on IP."""
    country_code = get_country_code(ip)
    if country_code in country_language_mapping:
        return country_language_mapping[country_code]
    return {'language': 'en', 'charset': 'utf-8'}  # Default values if country not found

# Example usage
ip_address = 'YOUR_IP_ADDRESS_HERE'  # Replace with the user's IP address
headers = get_default_headers(ip_address)
print(headers)
