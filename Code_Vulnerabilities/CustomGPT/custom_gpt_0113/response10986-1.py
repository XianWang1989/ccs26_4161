
import requests

# Function to get country code from IP
def get_country_code(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    data = response.json()
    return data.get('country')

# Mapping of countries to Accept-Language and Accept-Charset
language_mapping = {
    'US': ('en-US', 'UTF-8'),
    'FR': ('fr-FR', 'UTF-8'),
    'DE': ('de-DE', 'UTF-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'JP': ('ja-JP', 'UTF-8'),
    # Add more mappings as necessary
}

# Function to get default headers based on IP
def get_default_headers(ip):
    country_code = get_country_code(ip)
    if country_code in language_mapping:
        return {
            'Accept-Language': language_mapping[country_code][0],
            'Accept-Charset': language_mapping[country_code][1]
        }
    else:
        return {
            'Accept-Language': 'en-US',  # Default fallback
            'Accept-Charset': 'UTF-8'     # Default fallback
        }

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP
headers = get_default_headers(ip_address)
print(headers)
