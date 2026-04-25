
import requests

# Function to get country code from IP
def get_country_code(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    data = response.json()
    return data.get('country', '')

# Function to determine default headers based on country code
def get_default_headers(country_code):
    default_headers = {
        'US': {'Accept-Language': 'en-US,en;q=0.9', 'Accept-Charset': 'utf-8'},
        'FR': {'Accept-Language': 'fr-FR,fr;q=0.9', 'Accept-Charset': 'utf-8'},
        'RU': {'Accept-Language': 'ru-RU,ru;q=0.9', 'Accept-Charset': 'windows-1251'},
        # Add more mappings as needed
    }
    return default_headers.get(country_code, {'Accept-Language': 'en', 'Accept-Charset': 'utf-8'})

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP address
country_code = get_country_code(ip_address)
headers = get_default_headers(country_code)

print(headers)
