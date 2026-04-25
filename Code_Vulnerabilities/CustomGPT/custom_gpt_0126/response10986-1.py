
import requests

def get_country_code(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    if response.status_code == 200:
        data = response.json()
        return data.get('country')
    return None

def get_default_language_and_charset(country_code):
    # Mapping of country codes to default Accept-Language and Accept-Charset
    language_mapping = {
        'US': ('en-US', 'UTF-8'),
        'FR': ('fr-FR', 'UTF-8'),
        'DE': ('de-DE', 'UTF-8'),
        'RU': ('ru-RU', 'windows-1251'),
        # Add more country mappings as needed
    }
    return language_mapping.get(country_code, ('en', 'UTF-8'))  # Default to English if unknown

def determine_accept_headers(ip):
    country_code = get_country_code(ip)
    if country_code:
        default_language, default_charset = get_default_language_and_charset(country_code)
        return {
            'Accept-Language': default_language,
            'Accept-Charset': default_charset
        }
    return None

# Example usage
ip_address = 'YOUR_IP_ADDRESS'  # Replace with an actual IP address
headers = determine_accept_headers(ip_address)

if headers:
    print("Default Accept Headers:")
    print(headers)
else:
    print("Could not determine headers.")
