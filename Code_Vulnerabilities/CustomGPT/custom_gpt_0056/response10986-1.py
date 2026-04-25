
import requests

# Function to get the country code from an IP address
def get_country_code(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    data = response.json()
    return data.get('country')

# Mapping of country codes to default Accept-Language and Accept-Charset
country_language_mapping = {
    'US': ('en-US', 'utf-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'DE': ('de-DE', 'utf-8'),
    'FR': ('fr-FR', 'utf-8'),
    # Add more mappings as needed
}

def determine_default_headers(ip):
    country_code = get_country_code(ip)
    if country_code:
        language, charset = country_language_mapping.get(country_code, ('en', 'utf-8'))
        return {
            'Accept-Language': language,
            'Accept-Charset': charset
        }
    return None

# Example usage
ip_address = '8.8.8.8'  # Replace with the actual IP
default_headers = determine_default_headers(ip_address)
print(default_headers)
