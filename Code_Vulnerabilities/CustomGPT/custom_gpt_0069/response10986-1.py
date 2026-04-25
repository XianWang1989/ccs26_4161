
import requests

# Step 1: Get country code from IP
def get_country_code(ip_address):
    response = requests.get(f'https://ipinfo.io/{ip_address}/json')
    data = response.json()
    return data.get('country')  # Returns the country code (e.g., 'US', 'GB')

# Step 2: Map country codes to default headers
def get_default_headers(country_code):
    headers_map = {
        'US': ('en-US,en;q=0.5', 'UTF-8'),
        'GB': ('en-GB,en;q=0.5', 'UTF-8'),
        'RU': ('ru-RU,ru;q=0.5', 'windows-1251'),
        'FR': ('fr-FR,fr;q=0.5', 'UTF-8'),
        # Add more mappings as needed
    }
    return headers_map.get(country_code, ('en;q=0.5', 'UTF-8'))  # Default if not found

# Example usage
ip_address = '8.8.8.8'  # Replace with the actual IP address
country_code = get_country_code(ip_address)
accept_language, accept_charset = get_default_headers(country_code)

print(f'Default Accept-Language: {accept_language}')
print(f'Default Accept-Charset: {accept_charset}')
