
import requests

# Function to get the country code from IP
def get_country_code(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    data = response.json()
    return data.get('country_code')

# Mapping of country codes to default Accept-Language headers
country_to_lang = {
    'US': 'en-US,en;q=0.9',
    'GB': 'en-GB,en;q=0.9',
    'FR': 'fr-FR,fr;q=0.9',
    'DE': 'de-DE,de;q=0.9',
    'RU': 'ru-RU,ru;q=0.9',
    'CN': 'zh-CN,zh;q=0.9',
    # Add more mappings as needed
}

# Main function to determine default Accept-Language
def get_default_accept_language(ip):
    country_code = get_country_code(ip)
    return country_to_lang.get(country_code, 'en')  # Default to 'en' if country not found

# Example usage
ip_address = '8.8.8.8'  # Example IP address
default_language = get_default_accept_language(ip_address)
print(f'Default Accept-Language for IP {ip_address}: {default_language}')
