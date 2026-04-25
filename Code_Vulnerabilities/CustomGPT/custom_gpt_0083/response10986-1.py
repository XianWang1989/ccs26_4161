
import requests

# Function to get country code from IP address
def get_country_code(ip):
    response = requests.get(f'http://ip-api.com/json/{ip}')
    data = response.json()
    return data.get('countryCode')

# Function to get default Accept-Language header based on country code
def get_default_accept_language(country_code):
    language_map = {
        'US': 'en-US',
        'GB': 'en-GB',
        'FR': 'fr-FR',
        'DE': 'de-DE',
        'ES': 'es-ES',
        'IT': 'it-IT',
        'JP': 'ja-JP',
        'CN': 'zh-CN',
        'RU': 'ru-RU',
        'IN': 'hi-IN',
        'PT': 'pt-PT',
        'TR': 'tr-TR',
        'BG': 'bg-BG',
    }
    return language_map.get(country_code, 'en-US')  # Default to English if not found

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP address
country_code = get_country_code(ip_address)
accept_language = get_default_accept_language(country_code)

print(f'Default Accept-Language for IP {ip_address}: {accept_language}')
