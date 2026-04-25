
import requests

def get_country_from_ip(ip_address):
    """Get the country code from an IP address."""
    response = requests.get(f'https://ipapi.co/{ip_address}/json/')
    data = response.json()
    return data.get('country', 'Unknown')

def get_default_headers(country_code):
    """Map country code to default Accept-Language and Accept-Charset headers."""
    country_language_map = {
        'US': ('en-US', 'utf-8'),
        'RU': ('ru-RU', 'windows-1251'),
        'DE': ('de-DE', 'utf-8'),
        'FR': ('fr-FR', 'utf-8'),
        # Add more country mappings as needed
    }

    return country_language_map.get(country_code, ('en', 'utf-8'))

def main(ip_address):
    country_code = get_country_from_ip(ip_address)
    language, charset = get_default_headers(country_code)

    print(f"Default Accept-Language: {language}")
    print(f"Default Accept-Charset: {charset}")

# Example usage
ip = '8.8.8.8'  # Example IP address (Google Public DNS)
main(ip)
