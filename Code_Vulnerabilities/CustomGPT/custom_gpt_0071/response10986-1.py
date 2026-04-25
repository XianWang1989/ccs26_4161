
import requests

# Sample data: mapping of country codes to default Accept-Language and Accept-Charset
country_preferences = {
    'US': {'Accept-Language': 'en-US,en;q=0.9', 'Accept-Charset': 'utf-8'},
    'RU': {'Accept-Language': 'ru-RU,ru;q=0.9', 'Accept-Charset': 'windows-1251'},
    'DE': {'Accept-Language': 'de-DE,de;q=0.9', 'Accept-Charset': 'utf-8'},
    # Add other countries as needed
}

def get_country_code(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    data = response.json()
    return data['country']

def get_default_headers(ip):
    country_code = get_country_code(ip)
    return country_preferences.get(country_code, {'Accept-Language': 'en', 'Accept-Charset': 'utf-8'})

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP
headers = get_default_headers(ip_address)
print(headers)
