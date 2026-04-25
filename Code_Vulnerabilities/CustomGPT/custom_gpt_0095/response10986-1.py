
import requests

# Example mapping of country codes to typical Accept-Language headers
country_language_map = {
    'US': 'en-US,en;q=0.9',
    'GB': 'en-GB,en;q=0.9',
    'DE': 'de-DE,de;q=0.9',
    'FR': 'fr-FR,fr;q=0.9',
    'RU': 'ru-RU,ru;q=0.9',
    'CN': 'zh-CN,zh;q=0.9',
    # Add more countries as needed
}

def get_country_code(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/')
    if response.status_code == 200:
        return response.json().get('country')
    return None

def get_default_accept_language(ip_address):
    country_code = get_country_code(ip_address)
    if country_code and country_code in country_language_map:
        return country_language_map[country_code]
    return 'en'  # Default fallback

# Example usage
ip_address = '8.8.8.8'  # Replace with the desired IP address
accept_language = get_default_accept_language(ip_address)
print(f"Default Accept-Language for IP {ip_address}: {accept_language}")
