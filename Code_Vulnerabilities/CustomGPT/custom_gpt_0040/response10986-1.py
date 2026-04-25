
import requests

# Function to get country code from IP
def get_country_code(ip):
    response = requests.get(f'https://ipinfo.io/{ip}/json')
    if response.status_code == 200:
        data = response.json()
        return data.get('country')
    return None

# Mapping of country codes to Accept-Language and Accept-Charset
country_language_map = {
    'US': ('en-US', 'utf-8'),
    'GB': ('en-GB', 'utf-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'FR': ('fr-FR', 'utf-8'),
    'DE': ('de-DE', 'utf-8'),
    # Add more mappings as needed
}

# Function to determine default Accept-Language and Accept-Charset
def determine_headers(ip):
    country_code = get_country_code(ip)
    if country_code:
        lang, charset = country_language_map.get(country_code, ('en', 'utf-8'))
        return {
            'Accept-Language': lang,
            'Accept-Charset': charset
        }
    return None

# Example usage
ip_address = '8.8.8.8'  # Replace with the client's IP address
headers = determine_headers(ip_address)

if headers:
    print(f"Default headers for IP {ip_address}: {headers}")
else:
    print("Could not determine headers.")
