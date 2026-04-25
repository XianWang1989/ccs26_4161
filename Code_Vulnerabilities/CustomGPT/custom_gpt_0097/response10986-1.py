
import requests

# Function to get country code from IP
def get_country_code(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    data = response.json()
    return data.get('country', '')

# Function to determine default Accept-Language based on country code
def get_default_accept_language(country_code):
    language_mapping = {
        'US': ('en-US', 'UTF-8'),
        'FR': ('fr-FR', 'UTF-8'),
        'DE': ('de-DE', 'UTF-8'),
        'RU': ('ru-RU', 'windows-1251'),
        'CN': ('zh-CN', 'UTF-8'),
        # Add more mappings as needed
    }
    return language_mapping.get(country_code, ('en-US', 'UTF-8'))

# Example usage
ip_address = 'YOUR_IP_ADDRESS'  # Replace with actual IP
country_code = get_country_code(ip_address)
accept_language, charset = get_default_accept_language(country_code)

print(f"Country Code: {country_code}")
print(f"Accept-Language: {accept_language}")
print(f"Accept-Charset: {charset}")
